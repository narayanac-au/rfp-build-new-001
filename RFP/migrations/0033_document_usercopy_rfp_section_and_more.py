# Generated by Django 4.1.7 on 2023-04-11 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0032_alter_assuptionandrisk_topic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_usercopy',
            name='rfp_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RFP.rfpsection'),
        ),
        migrations.AlterField(
            model_name='extraimage',
            name='Industry',
            field=models.CharField(blank=True, choices=[('Agnostic', 'Agnostic'), ('Healthcare', 'Healthcare'), ('Finanace', 'Finanace'), ('HigherEducation', 'Higher Education')], default='Healthcare', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Agnostic', 'Agnostic'), ('Healthcare', 'Healthcare'), ('Finanace', 'Finanace'), ('HigherEducation', 'Higher Education')], default='Agnostic', max_length=100, null=True),
        ),
    ]