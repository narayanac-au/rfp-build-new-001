# Generated by Django 4.1 on 2023-05-16 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0047_userquestionans_document_usercopy_rfp_section_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="userstandardsection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("rfpid", models.CharField(blank=True, max_length=200, null=True)),
                ("country", models.CharField(blank=True, max_length=200, null=True)),
                ("industry", models.CharField(blank=True, max_length=200, null=True)),
                ("section", models.CharField(blank=True, max_length=200, null=True)),
                ("subsection", models.CharField(
                    blank=True, max_length=200, null=True)),
                ("question", models.TextField(blank=True, null=True)),
                (
                    "document",
                    models.FileField(blank=True, null=True,
                                     upload_to="media/"),
                ),
                ("image", models.FileField(blank=True, null=True, upload_to="media/")),
            ],
        )
    ]