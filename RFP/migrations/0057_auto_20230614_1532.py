# Generated by Django 3.2 on 2023-06-14 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RFP', '0056_document_usercopy_rfp_section_kpmggeo_displaykpmggeo_and_more'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='document_usercopy',
        #     name='rfp_section',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RFP.rfpsection'),
        # ),
        # migrations.AddField(
        #     model_name='image',
        #     name='title',
        #     field=models.CharField(blank=True, max_length=1000, null=True),
        # ),
        # migrations.AlterField(
        #     model_name='assuptionandrisk',
        #     name='category',
        #     field=models.CharField(blank=True, choices=[('Resources', 'Resources'), ('Data Migration', 'Data Migration'), ('Covid-19', 'Covid-19'), ('Integration', 'Integration'), ('Workday', 'Workday'), ('Software', 'Software'), ('Testing', 'Testing'), ('General', 'General'), ('Change Management', 'Change Management'), ('Deployment and Support', 'Deployment and Support')], default='General', max_length=100, null=True),
        # ),
        # migrations.AlterField(
        #     model_name='clientlogo',
        #     name='Industry',
        #     field=models.CharField(blank=True, choices=[('Finanace', 'Finanace'), ('Healthcare', 'Healthcare'), ('Agnostic', 'Agnostic'), ('HigherEducation', 'Higher Education')], default='Healthcare', max_length=100, null=True),
        # ),
        # migrations.AlterField(
        #     model_name='clientlogo',
        #     name='country',
        #     field=models.CharField(blank=True, choices=[('Australia', 'Australia'), ('US', 'US'), ('UK', 'UK')], default='Australia', max_length=100, null=True),
        # ),
        # migrations.AlterField(
        #     model_name='extraimage',
        #     name='country',
        #     field=models.CharField(blank=True, choices=[('Australia', 'Australia'), ('US', 'US'), ('UK', 'UK')], default='Australia', max_length=100, null=True),
        # ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, choices=[('Finanace', 'Finanace'), ('Healthcare', 'Healthcare'), ('Retail', 'Retail'), ('Transportation', 'Transportation'), ('Manufacturing', 'Manufacturing'), ('Higher Education', 'Education'), ('Energy', 'Energy'), ('Agnostic', 'Agnostic')], default='Agnostic', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kpmgadd',
            name='originaladdress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
