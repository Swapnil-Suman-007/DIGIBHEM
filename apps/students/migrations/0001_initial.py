

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentBulkUpload",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_uploaded", models.DateTimeField(auto_now=True)),
                ("csv_file", models.FileField(upload_to="students/bulkupload/")),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "current_status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=10,
                    ),
                ),
                ("registration_number", models.CharField(max_length=200, unique=True)),
                ("surname", models.CharField(max_length=200)),
                ("firstname", models.CharField(max_length=200)),
                ("other_name", models.CharField(blank=True, max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField(default=django.utils.timezone.now)),
                (
                    "date_of_admission",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("parent_mobile_number", models.CharField(blank=True, max_length=15)),
                ("address", models.TextField(blank=True)),
                ("others", models.TextField(blank=True)),
                (
                    "passport",
                    models.ImageField(blank=True, upload_to="students/passports/"),
                ),
                (
                    "current_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="corecode.StudentClass",
                    ),
                ),
            ],
            options={
                "ordering": ["surname", "firstname", "other_name"],
            },
        ),
    ]
