from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils.timezone import now

from governanceplatform.helpers import (
    is_observer_user,
    is_user_operator,
    is_user_regulator,
    user_in_group,
)
from governanceplatform.models import Functionality
from governanceplatform.settings import TERMS_ACCEPTANCE_TIME_IN_DAYS


class RestrictViewsMiddleware:
    """
    Middleware that blocks URLs depending the user group.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user_in_group(user, "PlatformAdmin"):
                if request.path.startswith("/incidents/") or request.path.startswith(
                    "/securityobjectives/"
                ):
                    return redirect("admin:index")

            if user_in_group(user, "IncidentUser"):
                if request.path.startswith("/securityobjectives/"):
                    return redirect("incidents")

            if is_user_regulator(user) and not request.session.get(
                "is_regulator_incidents", False
            ):
                if (
                    request.path == reverse("declaration")
                    or request.path.startswith("/incidents/delete/")
                    or request.path == reverse("create_workflow")
                ):
                    return redirect("incidents")
                if (
                    request.path.startswith("/securityobjectives/delete/")
                    or request.path.startswith("/securityobjectives/submit/")
                    or request.path.startswith("/securityobjectives/copy/")
                    or request.path == reverse("create_so_declaration")
                ):
                    return redirect("securityobjectives")

            if is_observer_user(user):
                if (
                    request.path == reverse("declaration")
                    or request.path == reverse("regulator_incidents")
                    or request.path.startswith("/incidents/delete/")
                    or request.path.startswith("/incidents/incident/")
                    or request.path == reverse("create_workflow")
                    or request.path == reverse("edit_workflow")
                    or request.path.startswith("/securityobjectives/")
                ):
                    return redirect("incidents")

            if is_user_operator(user):
                if request.path.startswith(
                    "/incidents/incident/"
                ) or request.path == reverse("regulator_incidents"):
                    return redirect(reverse("incidents"))
                if request.path == reverse("import_so_declaration"):
                    return redirect("securityobjectives")

        return self.get_response(request)


# check if the terms have been accepted
class TermsAcceptanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check for authenticated users
        if request.user.is_authenticated:
            # let the user logout and read terms
            if request.path == reverse("logout") or request.path == reverse("terms"):
                return self.get_response(request)
            if not request.user.accepted_terms and not request.path == reverse(
                "accept_terms"
            ):
                return redirect("accept_terms")
            # we want also to check the last checked
            if TERMS_ACCEPTANCE_TIME_IN_DAYS != 0:
                if (
                    request.user.accepted_terms_date is None
                    and not request.path == reverse("accept_terms")
                ):
                    return redirect("accept_terms")
                if (
                    request.user.accepted_terms_date is not None
                    and not request.path == reverse("accept_terms")
                ):
                    dt = now().date() - request.user.accepted_terms_date.date()
                    if dt.days > TERMS_ACCEPTANCE_TIME_IN_DAYS:
                        return redirect("accept_terms")
        return self.get_response(request)


# check if the regulator has access to functionality
class CheckFunctionalityAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            functionalities_types = Functionality.objects.filter(
                regulator__isnull=False
            ).values_list("type", flat=True)

            functionality_path = resolve(request.path).route.split("/")[0]
            if not Functionality.objects.filter(type=functionality_path).exists():
                return self.get_response(request)

            if functionality_path not in functionalities_types:
                return redirect("incidents")

            # regulator case
            if request.user.regulators.first() is not None:
                regulator = request.user.regulators.first()
                regulator_functionalities = regulator.functionalities.values_list(
                    "type", flat=True
                )
                if functionality_path not in regulator_functionalities:
                    return redirect("incidents")

        return self.get_response(request)
