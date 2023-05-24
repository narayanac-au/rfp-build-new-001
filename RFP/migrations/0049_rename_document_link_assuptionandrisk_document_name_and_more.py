# Generated by Django 4.1 on 2023-05-18 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0048_userstandardsection_document_usercopy_rfp_section_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assuptionandrisk",
            old_name="document_link",
            new_name="document_name",
        ),
        migrations.AddField(
            model_name="assuptionandrisk",
            name="description",
            field=models.TextField(blank=True, null=True),
        )
    ]
