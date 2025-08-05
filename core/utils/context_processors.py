"""Django context processors."""

import environ
import subprocess


from constance import config

from django.conf import settings

from users.models import CustomUser

env = environ.FileAwareEnv()


def export_vars(request) -> dict:
    """Export environment variables to Django templates.

    https://stackoverflow.com/questions/43207563/how-can-i-access-environment-variables-directly-in-a-django-template/43211490#43211490?newreg=9f02cb1a210c4f618f41fb1759bd9fb3

    Useage
    ------

    An example of how to access the environment variable in the template using
    just the data dict key to pass the CSS file location to the template.

    
    <link rel="stylesheet" href="{{ CSS }}">
    

    """

    data: dict = {}

    data["PROJECT_NAME"] = "wikhistory"

        # Add git short hash as GIT_VERSION
    try:
        git_version = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode("utf-8")
            .strip()
        )
    except Exception:
        git_version = "unknown"
    data["GIT_VERSION"] = git_version

    
    if settings.SETTINGS_MODULE == "config.settings.production":
        data["CSS"] = env("PROD_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css")
        data["TAILWIND_CSS_DEV"] = env("PROD_TAILWIND_CSS_DEV", default=False)

    elif settings.SETTINGS_MODULE == "config.settings.staging":
        data["CSS"] = env(
            "STAGING_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css"
        )
        data["TAILWIND_CSS_DEV"] = env("STAGING_TAILWIND_CSS_DEV", default=False)

    else:
        data["CSS"] = env(
            "LOCAL_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css"
        )
        data["TAILWIND_CSS_DEV"] = env("LOCAL_TAILWIND_CSS_DEV", default=True)
    

    
    
    data["ALLOW_NEW_USER_SIGNUP"] = config.ALLOW_NEW_USER_SIGNUP
    


    return data
