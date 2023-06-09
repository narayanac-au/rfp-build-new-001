# Generated by Django 3.1.2 on 2023-03-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0006_auto_20230313_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentapproval',
            name='approved',
            field=models.CharField(blank=True, default='No', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Healthcare', 'Healthcare'), ('Finanace', 'Finanace'), ('HigherEducation', 'Higher Education'), ('Agnostic', 'Agnostic')], default='Agnostic', max_length=100, null=True),
        ),
    ]
