# Generated by Django 2.2.3 on 2019-11-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("api", "0002_delete_pagepreview")]

    operations = [
        migrations.CreateModel(
            name="StubModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
            options={"managed": False},
        )
    ]
