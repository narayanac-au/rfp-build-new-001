# Generated by Django 4.1.7 on 2023-02-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RFP", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="document_usercopy",
            name="doc_index",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="document_usercopy",
            name="industry",
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
