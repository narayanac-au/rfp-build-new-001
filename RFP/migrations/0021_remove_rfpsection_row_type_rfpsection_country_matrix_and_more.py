# Generated by Django 4.1.7 on 2023-03-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0020_rfpsection_is_default_rfpsection_row_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfpsection',
            name='row_type',
        ),
        migrations.AddField(
            model_name='rfpsection',
            name='country_matrix',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='rfpsection',
            name='industry_matrix',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Finanace', 'Finanace'), ('Agnostic', 'Agnostic'), ('Healthcare', 'Healthcare'), ('HigherEducation', 'Higher Education')], default='Agnostic', max_length=100, null=True),
        ),
    ]
