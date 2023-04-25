from django_quill.fields import QuillField
from pyexpat import model
from django.db import models

# Create your models here.


class info(models.Model):

    clientfullname = models.CharField(max_length=200, null=True, blank=True)
    clientshortname = models.CharField(max_length=200, null=True, blank=True)
    clientindustry = models.CharField(max_length=200, null=True, blank=True)
    clientgeo = models.CharField(max_length=200, null=True, blank=True)

    KPMGgeo = models.CharField(max_length=200, null=True, blank=True)
    clientaddress_line1 = models.CharField(
        max_length=200, null=True, blank=True)
    clientaddress_line2 = models.CharField(
        max_length=200, null=True, blank=True)
    clientPostal_Code = models.CharField(max_length=200, null=True, blank=True)
    KPMGaddress1 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.clientshortname


class KPMGgeo(models.Model):
    id = models.AutoField(primary_key=True)
    KPMGgeo = models.CharField(max_length=200)

    def __str__(self):
        return self.KPMGgeo


class KPMGadd(models.Model):

    KPMGgeo = models.ForeignKey(KPMGgeo, on_delete=models.CASCADE)
    originaladdress = models.CharField(max_length=200)

    def __str__(self):
        return self.originaladdress


class Users(models.Model):

    user = models.CharField(max_length=200)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user


class Image(models.Model):

    imagechoices = {
        ('Agnostic', 'Agnostic'),
        ('Healthcare', 'Healthcare'),
        ('Finanace', 'Finanace'),
        ('HigherEducation', 'Higher Education'),

    }
    user = models.ManyToManyField(Users, null=True, blank=True)
    caption = models.CharField(
        max_length=100, null=True, blank=True, default='Agnostic', choices=imagechoices)
    image = models.ImageField(
        null=True, blank=True, upload_to="./media/")
    upload = models.FileField(
        null=True, blank=True, upload_to='./media/')
    cloud_link = models.CharField(max_length=500, null=True, blank=True)
    selected = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.caption


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(Users, null=True, blank=True)
    rfp_id = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    industry = models.CharField(max_length=50, null=False, blank=False)
    Section = models.TextField(null=True, blank=True)
    Sub_Section = models.TextField(null=True, blank=True)
    Questions = models.TextField(null=True, blank=True)
    options1 = models.TextField(null=True, blank=True)
    options2 = models.TextField(null=True, blank=True)
    options3 = models.TextField(null=True, blank=True)
    Tick1 = models.CharField(max_length=10, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    Model_Image_Link_BLOB = models.URLField(
        max_length=200, null=True, blank=True)
    Binaryword = models.BinaryField(null=True, blank=True)
    Binarypic = models.BinaryField(null=True, blank=True)
    File = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.country


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    industry = models.CharField(max_length=50, null=False, blank=False)
    doc_index = models.CharField(max_length=100, null=True, blank=True)
    user = models.ManyToManyField(Users, blank=True)
    selected = models.CharField(max_length=10, null=True, blank=True)
    File = models.FileField(upload_to='files', null=True, blank=True)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return self.doc_index


class askques(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True, unique=True)
    selected = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    clientgeo = models.CharField(max_length=200, null=True, blank=True)
    picup = models.ImageField(upload_to='pickupdir/')

    def __str__(self):
        return self.user


class First_Page_upload(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    clientgeo = models.CharField(max_length=200, null=True, blank=True)
    picdown = models.ImageField(upload_to='First_page_upload/Drop')

    def __str__(self):
        return self.user


class First_Page(models.Model):
    id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=50, null=False, blank=False)
    pic1 = models.ImageField(upload_to='First_page_upload/Manual')
    pic2 = models.ImageField(upload_to='First_page_upload/Manual')
    pic3 = models.ImageField(upload_to='First_page_upload/Manual')
    options1 = models.CharField(max_length=10, null=True, blank=True)
    options2 = models.CharField(max_length=10, null=True, blank=True)
    options3 = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.industry


class UserQuery(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    rfp_id = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=50, null=True, blank=True)
    Section = models.TextField(null=True, blank=True)
    Sub_Section = models.TextField(null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    answer1 = models.TextField(null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    sentapproval = models.CharField(max_length=50, null=True, blank=True)
    approved = models.CharField(max_length=50, null=True, blank=True)
    viewed = models.CharField(max_length=50, null=True, blank=True)
    # approved=models.BooleanField('Approved',default=False,null=True,blank=True)

    def __str__(self):
        return self.query


class DropQuery(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    answer1 = models.TextField(null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    select1 = models.CharField(max_length=10, null=True, blank=True)
    select2 = models.CharField(max_length=10, null=True, blank=True)
    select3 = models.CharField(max_length=10, null=True, blank=True)
    optionselect = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.question


class SelectDropQuery(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    answer1 = models.TextField(null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    select1 = models.CharField(max_length=10, null=True, blank=True)
    select2 = models.CharField(max_length=10, null=True, blank=True)
    select3 = models.CharField(max_length=10, null=True, blank=True)
    optionselect = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.question


class UserQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    rfp_id = models.CharField(max_length=50, null=True, blank=True)
    content_type = models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    Section = models.TextField(null=True, blank=True)
    Sub_Section = models.TextField(null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    Document_link = models.FileField(null=True)

    Approved = models.BooleanField(
        'Approved', default=False, null=True, blank=True)

    def __str__(self):
        return self.question


class Approval(models.Model):
    id = models.AutoField(primary_key=True)
    rfp_id = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    industry = models.CharField(max_length=50, null=False, blank=False)
    Section = models.TextField(null=True, blank=True)
    Sub_Section = models.TextField(null=True, blank=True)
    Questions = models.TextField(null=True, blank=True)
    options1 = models.TextField(null=True, blank=True)
    options2 = models.TextField(null=True, blank=True)
    options3 = models.TextField(null=True, blank=True)
    approved = models.BooleanField(
        'Approved', default=False, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    Model_Image_Link_BLOB = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.approved


class project(models.Model):
    name = models.CharField(max_length=200)
    content = QuillField(default="Hello")

    def __str__(self):
        return self.name


class documentapproval(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    clientgeo = models.CharField(max_length=200, null=True, blank=True)
    documentapproval = models.ImageField(upload_to='pickupdir/')
    approved = models.CharField(
        max_length=200, default="No", null=True, blank=True)

    def __str__(self):
        return self.user


class RfpSection(models.Model):
    id = models.AutoField(primary_key=True)
    rfpid = models.CharField(max_length=5000, null=True, blank=True)
    content_type = models.CharField(max_length=5000, null=True, blank=True)
    industry = models.CharField(max_length=5000, null=True, blank=True)
    country = models.CharField(max_length=5000, null=True, blank=True)
    section_data = models.CharField(max_length=5000, null=True, blank=True)
    sub_section = models.CharField(max_length=5000, null=True, blank=True)
    question = models.CharField(max_length=5000, null=True, blank=True)
    document_link = models.CharField(max_length=5000, null=True, blank=True)
    document_file_name = models.CharField(max_length=5000, null=True, blank=True)
    image_link = models.CharField(max_length=5000, null=True, blank=True)
    user = models.ManyToManyField(Users, blank=True)
    order = models.IntegerField(null=True, blank=True)
    country_matrix = models.CharField(max_length=10, blank=True, null=True)
    industry_matrix = models.CharField(max_length=10, blank=True, null=True)

    is_default = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.rfpid}-{self.country}-{self.industry}'


class RfpData(models.Model):
    id = models.AutoField(primary_key=True)
    rfpid = models.CharField(max_length=5000, null=True, blank=True)
    rfp_resource_name = models.CharField(
        max_length=5000, null=True, blank=True)
    industry = models.CharField(max_length=5000, null=True, blank=True)
    country = models.CharField(max_length=5000, null=True, blank=True)
    section_data = models.CharField(max_length=5000, null=True, blank=True)
    question = models.CharField(max_length=5000, null=True, blank=True)
    document_link = models.CharField(max_length=5000, null=True, blank=True)
    image_link = models.CharField(max_length=5000, null=True, blank=True)
    content_type = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f'{self.rfpid}-{self.country}-{self.industry}'


class Document_usercopy(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    industry = models.CharField(max_length=50, null=False, blank=False)
    doc_index = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=200, blank=True)
    rfp_section = models.ForeignKey(
        RfpSection, blank=True, null=True, on_delete=models.CASCADE
    )
    File = models.FileField(upload_to='files', null=True, blank=True)
    file_link = models.CharField(max_length=500, null=True, blank=True)
    matrix = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'<{self.country}-{self.industry}-{self.user}>'


class RfpDocuments(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    industry = models.CharField(max_length=50, null=False, blank=False)
    user = models.CharField(max_length=200, blank=True)
    rfp_file = models.FileField(upload_to='files/rfp_documents', null=True, blank=True)

    def __str__(self):
        return f'<{self.country}-{self.industry}-{self.user}-{self.rfp_file.name}>'


class ExtraImage(models.Model):

    countrychoices = {
        ('Australia', 'Australia'),
        ('US', 'US'),
        ('UK', 'UK'),
    }

    imagechoices = {
        ('Agnostic', 'Agnostic'),
        ('Healthcare', 'Healthcare'),
        ('Finanace', 'Finanace'),
        ('HigherEducation', 'Higher Education'),

    }
    user = models.ManyToManyField(Users, blank=True)
    country = models.CharField(
        max_length=100, null=True, blank=True, default='Australia', choices=countrychoices)
    Industry = models.CharField(
        max_length=100, null=True, blank=True, default='Healthcare', choices=imagechoices)
    image = models.ImageField(
        null=True, blank=True, upload_to="./media/")

    selected = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.country


class ImageUpload(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    clientgeo = models.CharField(max_length=200, null=True, blank=True)
    picup = models.ImageField(upload_to='imgdir/')

    def __str__(self):
        return self.user


class AssuptionAndRisk(models.Model):
    id = models.AutoField(primary_key=True)
    countrychoices = {
        ('Australia', 'Australia'),
        ('US', 'US'),
        ('UK', 'UK'),


    }
    imagechoices = {
        ('Assuption_And_Risk', 'Assuption_And_Risk'),
        ('Key_consideration_and_risk', 'Key_consideration_and_risk'),

    }
    user = models.ManyToManyField(Users, blank=True)
    Topic = models.CharField(
        max_length=100, null=True, blank=True, default='Assuption_And_Risk', choices=imagechoices)
    country = models.CharField(
        max_length=100, null=True, blank=True, default='Australia', choices=countrychoices)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.country


class SectionExtraImage(models.Model):

    user = models.ManyToManyField(Users, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    industry = models.CharField(max_length=1000, null=True, blank=True)
    section_data = models.CharField(max_length=1000, null=True, blank=True)
    image_link = models.CharField(max_length=1000, null=True, blank=True)

    selected = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.country
