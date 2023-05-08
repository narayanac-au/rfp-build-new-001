# Generated by Django 4.1 on 2023-05-06 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0040_document_usercopy_rfp_section_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="logoUpload",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("clientgeo", models.CharField(
                    blank=True, max_length=200, null=True)),
                ("picup", models.ImageField(upload_to="logodir/")),
            ],
        )
    ]
