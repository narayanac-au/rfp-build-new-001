from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class RfpSection_admin(ImportExportModelAdmin):
    list_display = ['country', 'industry', 'section_data']


class info_admin(ImportExportModelAdmin):
    list_display = ['clientfullname', 'clientshortname', 'clientindustry',
                    'clientgeo', 'clientaddress_line1', 'clientaddress_line2',
                    'clientPostal_Code', 'KPMGaddress1', 'KPMGgeo']


class KPMGgeo_admin(ImportExportModelAdmin):
    list_display = ['KPMGgeo']


class KPMGadd_admin(ImportExportModelAdmin):
    list_display = ['KPMGgeo', 'originaladdress']


class Question_admin(ImportExportModelAdmin):
    list_display = ['id', 'rfp_id', 'country', 'industry', 'Questions', 'options1',
                    'options2', 'options3', 'Tick1', 'Model_Image_Link_BLOB', 'answer', 'Binaryword', 'Binarypic', 'File']


class Users_admin(ImportExportModelAdmin):
    list_display = ['user']


class Images_admin(ImportExportModelAdmin):
    list_display = ['caption', 'image', 'selected']


class Document_admin(ImportExportModelAdmin):
    list_display = ['id', 'country', 'industry',
                    'doc_index', 'selected']


class DocumentUserCopy_admin(ImportExportModelAdmin):
    list_display = ['id', 'country', 'industry',
                    'doc_index']


class askques_admin(ImportExportModelAdmin):
    list_display = ['user', 'selected']


class Product_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'picup', 'clientgeo']


class UserQuery_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'query', 'answer1', 'answer2',
                    'answer3', 'sentapproval', 'approved', 'viewed']


class First_Page_upload_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'picdown', 'clientgeo']


class FirstPage_admin(ImportExportModelAdmin):
    list_display = ['industry', 'pic1', 'pic2',
                    'pic3', 'options1', 'options2', 'options3']


class DropQuery_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'question', 'answer1', 'answer2',
                    'answer3', 'optionselect', 'select1', 'select2', 'select3']


class SelectDropQuery_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'question', 'answer1', 'answer2',
                    'answer3', 'optionselect', 'select1', 'select2', 'select3']


class UserQuestion_admin(ImportExportModelAdmin):
    list_display = ['id', 'rfp_id', 'content_type', 'country', 'industry',
                    'Section', 'Sub_Section', 'question', 'Document_link', 'Approved']


class approval_admin(ImportExportModelAdmin):
    list_display = ['id', 'rfp_id', 'country', 'industry', 'Section',
                    'Sub_Section', 'Questions', 'options1', 'options2', 'options3', 'approved']


class project_admin(ImportExportModelAdmin):
    list_display = ['name', 'content']


class documentapproval_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'clientgeo', 'documentapproval', 'approved']


class ExtraImages_admin(ImportExportModelAdmin):
    list_display = ['Industry', 'image', 'selected']


class ImageUpload_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'clientgeo', 'picup']


class ImageUpload_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'clientgeo', 'picup', 'approved']


class AssuptionAndRisk_admin(ImportExportModelAdmin):
    list_display = ['id', 'Topic', 'country', 'Description']


class SectionExtraImage_admin(ImportExportModelAdmin):
    list_display = ['id', 'country', 'industry',
                    'section_data', 'image_link', 'selected']


class notsatisfieddoc_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'docup', 'clientgeo', 'query']


class clientlogo_admin(ImportExportModelAdmin):
    list_display = ['Industry', 'logo', 'selected']


class logoUpload_admin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'clientgeo', 'picup', 'approved']


admin.site.register(project, project_admin)
admin.site.register(info, info_admin)
admin.site.register(KPMGgeo, KPMGgeo_admin)
admin.site.register(KPMGadd, KPMGadd_admin)
admin.site.register(Question, Question_admin)
admin.site.register(Document, Document_admin)
admin.site.register(Users, Users_admin)
admin.site.register(Image, Images_admin)
admin.site.register(askques, askques_admin)
admin.site.register(Product, Product_admin)
admin.site.register(UserQuery, UserQuery_admin)
admin.site.register(First_Page_upload, First_Page_upload_admin)
admin.site.register(First_Page, FirstPage_admin)
admin.site.register(DropQuery, DropQuery_admin)
admin.site.register(SelectDropQuery, SelectDropQuery_admin)
admin.site.register(UserQuestion, UserQuestion_admin)
admin.site.register(Approval, approval_admin)
admin.site.register(Document_usercopy, DocumentUserCopy_admin)
admin.site.register(documentapproval, documentapproval_admin)
admin.site.register(RfpSection, RfpSection_admin)
admin.site.register(ExtraImage, ExtraImages_admin)
admin.site.register(ImageUpload, ImageUpload_admin)
admin.site.register(AssuptionAndRisk, AssuptionAndRisk_admin)
admin.site.register(SectionExtraImage, SectionExtraImage_admin)
admin.site.register(notsatisfieddoc, notsatisfieddoc_admin)
admin.site.register(clientlogo, clientlogo_admin)
admin.site.register(logoUpload, logoUpload_admin)
