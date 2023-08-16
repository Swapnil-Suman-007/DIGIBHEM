

from django.db import migrations
from django.contrib.auth.models import User


def default_site_config(apps, schema_editor):
    """Default site configurations"""

    User.objects.create_superuser("admin", "admin@schoolapp.com", "admin123")

    Config = apps.get_model("corecode", "SiteConfig")
    Config.objects.bulk_create(
        [
            Config(key="school_name", value="My School"),
            Config(key="school_slogan", value="A great school"),
            Config(key="school_address", value="Lagos, Nigeria"),
        ]
    )

    Session = apps.get_model("corecode", "AcademicSession")
    Session.objects.bulk_create(
        [
            Session(name="2019/2020", current=True),
        ]
    )

    Term = apps.get_model("corecode", "AcademicTerm")
    Term.objects.bulk_create(
        [
            Term(name="1st Term", current=True),
            Term(name="2nd Term", current=False),
            Term(name="3rd Term", current=False),
        ]
    )

    Subject = apps.get_model("corecode", "Subject")
    Subject.objects.bulk_create(
        [
            Subject(name="Mathematics"),
            Subject(name="English"),
        ]
    )

    StudentClass = apps.get_model("corecode", "StudentClass")
    StudentClass.objects.bulk_create(
        [
            StudentClass(name="JSS 1"),
            StudentClass(name="JSS 2"),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(default_site_config),
    ]
