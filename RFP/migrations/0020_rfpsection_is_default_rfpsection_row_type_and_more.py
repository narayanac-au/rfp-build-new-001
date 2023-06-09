# Generated by Django 4.1.7 on 2023-03-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0019_alter_document_usercopy_file_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpsection',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rfpsection',
            name='row_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Finanace', 'Finanace'), ('Agnostic', 'Agnostic'), ('HigherEducation', 'Higher Education'), ('Healthcare', 'Healthcare')], default='Agnostic', max_length=100, null=True),
        ),
    ]
