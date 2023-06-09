# Generated by Django 4.1.7 on 2023-02-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0003_remove_document_usercopy_user_document_usercopy_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="caption",
            field=models.CharField(
                blank=True,
                choices=[
                    ("F", "Finanace"),
                    ("A", "Agnostic"),
                    ("HE", "Higher Education"),
                    ("H", "Healthcase"),
                ],
                default="A",
                max_length=100,
                null=True,
            ),
        ),
    ]
