# Generated by Django 4.1 on 2023-05-10 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0045_document_usercopy_rfp_section_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assuptionandrisk",
            old_name="file_link",
            new_name="document_link",
        ),
        migrations.RemoveField(
            model_name="assuptionandrisk", name="Description",),
        migrations.RemoveField(model_name="assuptionandrisk", name="Topic",),
        migrations.AddField(
            model_name="assuptionandrisk",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Deployment and Support", "Deployment and Support"),
                    ("Resources", "Resources"),
                    ("Data Migration", "Data Migration"),
                    ("Testing", "Testing"),
                    ("Integration", "Integration"),
                    ("Software", "Software"),
                    ("Covid-19", "Covid-19"),
                    ("Workday", "Workday"),
                    ("Change Management", "Change Management"),
                    ("General", "General"),
                ],
                default="General",
                max_length=100,
                null=True,
            ),
        ),

    ]
