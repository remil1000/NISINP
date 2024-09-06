from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.signals import user_logged_in
from governanceplatform.models import User

from .models import ObserverUser, RegulatorUser, SectorCompanyContact
from .permissions import (
    set_observer_admin_permissions,
    set_observer_user_permissions,
    set_operator_admin_permissions,
    set_operator_user_permissions,
    set_regulator_admin_permissions,
    set_regulator_staff_permissions,
)

from .helpers import user_in_group


# Add logs for user connection
def add_log_for_connection(sender, user, request, **kwargs):
    if (
        user_in_group(user, "RegulatorAdmin")
        or user_in_group(user, "RegulatorUser")
        or user_in_group(user, "PlatformAdmin")
    ):
        LogEntry.objects.log_action(
            user_id=user.id,
            content_type_id=ContentType.objects.get_for_model(User).pk,
            object_id=user.id,
            object_repr=user.email,
            action_flag=5,
        )


user_logged_in.connect(add_log_for_connection)


@receiver(post_save, sender=SectorCompanyContact)
def update_user_groups(sender, instance, created, **kwargs):
    user = instance.user
    user.is_staff = False
    user.is_superuser = False

    some_company_is_administrator = user.sectorcompanycontact_set.filter(
        is_company_administrator=True
    )

    # Operator Administrator permission
    if some_company_is_administrator.exists():
        set_operator_admin_permissions(user)
    else:
        set_operator_user_permissions(user)
        return


@receiver(post_save, sender=RegulatorUser)
def update_regulator_user_groups(sender, instance, created, **kwargs):
    user = instance.user
    user.is_staff = False
    user.is_superuser = False

    # Regulator Administrator permissions
    if instance.is_regulator_administrator:
        set_regulator_admin_permissions(user)
        return
    else:
        set_regulator_staff_permissions(user)
        return


@receiver(post_save, sender=ObserverUser)
def update_observer_user_groups(sender, instance, created, **kwargs):
    user = instance.user
    user.is_staff = False
    user.is_superuser = False

    # Regulator Administrator permissions
    if instance.is_observer_administrator:
        set_observer_admin_permissions(user)
        return
    else:
        set_observer_user_permissions(user)
        return


@receiver(post_delete, sender=SectorCompanyContact)
@receiver(post_delete, sender=RegulatorUser)
@receiver(post_delete, sender=ObserverUser)
def delete_user_groups(sender, instance, **kwargs):
    user = instance.user
    group_names = [
        "PlatformAdmin",
        "RegulatorAdmin",
        "RegulatorUser",
        "OperatorAdmin",
        "OperatorUser",
        "IncidentUser",
        "ObserverAdmin",
        "ObserverUser",
    ]

    for group_name in group_names:
        try:
            group = Group.objects.get(name=group_name)
        except ObjectDoesNotExist:
            group = None

        if group and user.groups.filter(name=group_name).exists():
            # remove roles only if there is no linked company/regulator
            if group_name == "OperatorAdmin" and user.companies.count() < 1:
                user.groups.remove(group)
                new_group, created = Group.objects.get_or_create(name="OperatorUser")
                if new_group:
                    user.groups.add(new_group)

                user.is_active = False

            if group_name == "RegulatorAdmin" and user.regulators.count() < 1:
                user.groups.remove(group)
                new_group, created = Group.objects.get_or_create(name="RegulatorUser")
                if new_group:
                    user.groups.add(new_group)
                user.is_active = False

    if not user.sectorcompanycontact_set.exists():
        user.is_staff = False
        user.is_superuser = False

    user.save()
