

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0003_auto_20200726_0925"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicsession",
            name="current",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="academicterm",
            name="current",
            field=models.BooleanField(default=True),
        ),
    ]
