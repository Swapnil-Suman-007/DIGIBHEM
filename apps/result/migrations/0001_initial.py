

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("students", "0001_initial"),
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Result",
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
                ("test_score", models.IntegerField(default=0)),
                ("exam_score", models.IntegerField(default=0)),
                (
                    "current_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.StudentClass",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.AcademicSession",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.Student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.Subject",
                    ),
                ),
                (
                    "term",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.AcademicTerm",
                    ),
                ),
            ],
            options={
                "ordering": ["subject"],
            },
        ),
    ]
