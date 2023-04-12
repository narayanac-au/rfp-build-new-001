# Generated by Django 3.2 on 2023-03-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0009_auto_20230325_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Agnostic', 'Agnostic'), ('Finanace', 'Finanace'), ('Healthcare', 'Healthcare'), ('HigherEducation', 'Higher Education')], default='Agnostic', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rfpdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rfpsection',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
