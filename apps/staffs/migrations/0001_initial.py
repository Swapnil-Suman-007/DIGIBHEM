

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
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
                ("mobile_number", models.CharField(blank=True, max_length=15)),
                ("address", models.TextField(blank=True)),
                ("others", models.TextField(blank=True)),
            ],
        ),
    ]
