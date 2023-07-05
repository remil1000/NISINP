from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django_otp import devices_for_user
from django_otp.decorators import otp_required
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from parler.admin import TranslatableAdmin

from .models import (
    Company,
    CompanyAdministrator,
    Functionality,
    OperatorType,
    Sector,
    SectorContact,
    Services,
    User,
)
from .settings import SITE_NAME


# Customize the admin site
class CustomAdminSite(admin.AdminSite):
    site_header = SITE_NAME + " " + _("Administration")
    site_title = SITE_NAME

    def admin_view(self, view, cacheable=False):
        decorated_view = otp_required(view)
        return super().admin_view(decorated_view, cacheable)


admin_site = CustomAdminSite()


class SectorResource(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    name = fields.Field(
        column_name="name",
        attribute="name",
    )

    parent = fields.Field(
        column_name="parent",
        attribute="parent",
        widget=ForeignKeyWidget(Sector, field="name"),
    )

    class Meta:
        model = Sector


@admin.register(Sector, site=admin_site)
class SectorAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["name", "parent"]
    search_fields = ["name"]
    resource_class = SectorResource


class ServicesResource(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    name = fields.Field(
        column_name="name",
        attribute="name",
    )

    sector = fields.Field(
        column_name="sector",
        attribute="sector",
        widget=ForeignKeyWidget(Sector, field="name"),
    )

    class Meta:
        model = Sector


@admin.register(Services, site=admin_site)
class ServicesAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["name", "sector"]
    search_fields = ["name"]
    resource_class = ServicesResource


class CompanyResource(resources.ModelResource):
    id = fields.Field(column_name="id", attribute="id")
    identifier = fields.Field(column_name="identifier", attribute="identifier")
    name = fields.Field(column_name="name", attribute="name")
    address = fields.Field(column_name="address", attribute="address")
    country = fields.Field(column_name="country", attribute="country")
    email = fields.Field(column_name="email", attribute="email")
    phone_number = fields.Field(column_name="phone_number", attribute="phone_number")
    is_regulator = fields.Field(column_name="is_regulator", attribute="is_regulator")
    monarc_path = fields.Field(column_name="monarc_path", attribute="monarc_path")
    sectors = fields.Field(
        column_name="sectors",
        attribute="sectors",
        widget=ManyToManyWidget(Sector, field="name", separator=","),
    )

    class Meta:
        model = Company


class companySectorInline(admin.TabularInline):
    model = Company.sectors.through
    verbose_name = _("sector")
    verbose_name_plural = _("sectors")
    extra = 1


class CompanySectorListFilter(SimpleListFilter):
    title = _("Sectors")
    parameter_name = "sectors"

    def lookups(self, request, model_admin):
        sectors = Sector.objects.all()
        if not request.user.is_superuser:
            sectors = sectors.filter(id__in=request.user.sectors.all())
        return [(sector.id, sector.name) for sector in sectors]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(companies=value)
        return queryset


@admin.register(Company, site=admin_site)
class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CompanyResource
    list_display = [
        "name",
        "address",
        "country",
        "email",
        "phone_number",
        "get_sectors",
        "is_regulator",
    ]
    list_filter = ["is_regulator", CompanySectorListFilter]
    search_fields = ["name"]
    inlines = (companySectorInline,)
    fieldsets = [
        (
            _("Contact Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "name",
                    ("address", "country"),
                    ("email", "phone_number"),
                ],
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "is_regulator",
                ],
            },
        ),
        (
            _("Configuration Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "identifier",
                    "monarc_path",
                ],
            },
        ),
    ]

    def get_list_filter(self, request):
        list_filter = super().get_list_filter(request)
        if not request.user.is_superuser:
            list_filter = [field for field in list_filter if field != "is_regulator"]

        return list_filter

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        # Check if the user is a superuser
        if not request.user.is_superuser:
            fieldsets = [
                fieldset for fieldset in fieldsets if fieldset[0] != _("Permissions")
            ]

        return fieldsets

    def get_list_display(self, request):
        list_display = super().get_list_display(request)

        # Check user permissions
        if not request.user.is_superuser:
            list_display = [
                field for field in list_display if field not in ("is_regulator")
            ]

        return list_display

    def get_readonly_fields(self, request, obj=None):
        # Get the original read-only fields
        readonly_fields = super().get_readonly_fields(request, obj)

        if not request.user.is_superuser:
            readonly_fields = (
                "identifier",
                "monarc_path",
            )

        return readonly_fields

    def get_queryset(self, request):
        # Get the original queryset
        queryset = super().get_queryset(request)

        # Filter the queryset based on the user's related companies
        if request.user.is_superuser:
            return queryset  # Superuser can see all companies
        else:
            return queryset.filter(companyadministrator__user=request.user)


class UserResource(resources.ModelResource):
    id = fields.Field(column_name="id", attribute="id")
    first_name = fields.Field(column_name="first_name", attribute="first_name")
    last_name = fields.Field(column_name="last_name", attribute="last_name")
    email = fields.Field(column_name="email", attribute="email")
    phone_number = fields.Field(column_name="phone_number", attribute="phone_number")
    companies = fields.Field(
        column_name="companies",
        attribute="companies",
        widget=ManyToManyWidget(Company, field="name", separator=","),
    )
    sectors = fields.Field(
        column_name="sectors",
        attribute="sectors",
        widget=ManyToManyWidget(Sector, field="name", separator=","),
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "companies",
            "sectors",
        ]


class userSectorInline(admin.TabularInline):
    model = SectorContact
    verbose_name = _("sector")
    verbose_name_plural = _("sectors")
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sector":
            if request.user.is_superuser:
                # Display all available sectors for the superuser
                kwargs["queryset"] = Sector.objects.all()
            else:
                # Filter the choices by the current user's associated sectors
                kwargs["queryset"] = request.user.sectors.all()
            return super().formfield_for_foreignkey(db_field, request, **kwargs)


class userCompanyInline(admin.TabularInline):
    model = CompanyAdministrator
    verbose_name = _("company")
    verbose_name_plural = _("companies")
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if request.user.is_superuser:
                # Display all available companies for the superuser
                kwargs["queryset"] = Company.objects.all()
            else:
                # Filter the choices by the current user's associated companies
                kwargs["queryset"] = request.user.companies.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.empty_permitted = False
        return formset


# reset the 2FA we delete the TOTP devices
@admin.action(description=_("Reset 2FA"))
def reset_2FA(modeladmin, request, queryset):
    for user in queryset:
        devices = devices_for_user(user)
        for device in devices:
            device.delete()


class UserCompaniesListFilter(SimpleListFilter):
    title = _("Companies")
    parameter_name = "companies"

    def lookups(self, request, model_admin):
        companies = Company.objects.all()
        if not request.user.is_superuser:
            companies = companies.filter(id__in=request.user.companies.all())
        return [(company.id, company.name) for company in companies]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(companies=value)
        return queryset


class UserSectorListFilter(SimpleListFilter):
    title = _("Sectors")
    parameter_name = "sectors"

    def lookups(self, request, model_admin):
        sectors = Sector.objects.all()
        if not request.user.is_superuser:
            sectors = sectors.filter(id__in=request.user.sectors.all())
        return [(sector.id, sector.name) for sector in sectors]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(companies=value)
        return queryset


@admin.register(User, site=admin_site)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "get_companies",
        "get_sectors",
        "is_staff",
    ]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = [
        UserCompaniesListFilter,
        UserSectorListFilter,
        "is_staff",
    ]
    list_display_links = ("email", "first_name", "last_name")
    inlines = [userCompanyInline, userSectorInline]
    filter_horizontal = ("groups",)
    fieldsets = [
        (
            _("Contact Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    ("first_name", "last_name"),
                    ("email", "phone_number"),
                ],
            },
        ),
    ]
    actions = [reset_2FA]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Filter the queryset based on the user's related companies
        if request.user.is_superuser:
            return queryset

        if user_in_group(request.user, "RegulatorStaff"):
            return queryset.filter(
                companies__in=request.user.sectors.all(),
            )

        return queryset.filter(
            companies__in=request.user.companies.all(),
        )


class FunctionalityResource(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    name = fields.Field(
        column_name="name",
        attribute="name",
    )


@admin.register(Functionality, site=admin_site)
class FunctionalityAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    resource_class = FunctionalityResource


class OperatorTypeResource(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    type = fields.Field(
        column_name="type",
        attribute="type",
    )

    functionalities = fields.Field(
        column_name="functionalities",
        attribute="functionalities",
        widget=ForeignKeyWidget(Functionality, field="name"),
    )

    class Meta:
        model = Functionality


@admin.register(OperatorType, site=admin_site)
class OperatorTypeAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["type"]
    search_fields = ["type"]
    resource_class = OperatorTypeResource


def user_in_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return user.groups.filter(id=group.id).exists()
    except Group.DoesNotExist:
        return False
