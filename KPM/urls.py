"""KPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from RFP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="index"),
    path('first/', include('RFP.urls')),
    path('second/', include('RFP.urls')),
    path('pre/', include('RFP.urls')),
    path('info/', include('RFP.urls')),
    path('doc/', include('RFP.urls')),
    path('pdf/', include('RFP.urls')),
    path('start/', include('RFP.urls')),
    path('download/', include('RFP.urls')),
    path('drop/', include('RFP.urls')),

    path('<int:id>/', views.editans_view,
         name="editans"),  # {% url 'editans' %}
    path('a/<int:id>/', views.drop_editans_view,
         name="drop_editans"),  # {% url 'drop_editans' %}s

    path('file/', include('RFP.urls')),
    path('droprfp/', include('RFP.urls')),
    path('drp/', include('RFP.urls')),
    path('approve/', include('RFP.urls')),
    path('confirmation/', include('RFP.urls')),
    path('ar/', include('RFP.urls')),
    path('dr/', include('RFP.urls')),
    path('login/', views.login, name="login"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('loginapprover/', views.loginapprover, name="loginapprover"),
    path('approversignup/', views.approversignup, name="approversignup"),
    path('binary/', include('RFP.urls')),
    path('geo/', include('RFP.urls')),
    path('chat/', include('RFP.urls')),
    path('Selected/', include('RFP.urls')),
    path('Onscreen/', include('RFP.urls')),
    path('ExtraImage/', views.ExtraImage_view, name="extraimage"),
    path('UploadExtraImage/', views.UploadExtraImage_view, name="UploadExtraImage"),
    path('Uploadassumprisk/', views.Uploadassumprisk_view, name="Uploadassumprisk"),
    path('imageuploadmodel/', views.image_upload_view, name="imageuploadmodel"),
    path('AssuptionAndRisk/', views.AssuptionAndRisk_view,
         name="AssuptionAndRisk"),
    path('Assumption_upload/', views.Assumption_upload_view,
         name="Assumption_upload"),
    path('notsatisfieddoc/', views.notsatisfieddoc_view, name="notsatisfieddoc"),
    path('clientlogo/', views.clientlogo_view, name="clientlogo"),
    path('UploadClientlogo/', views.logo_upload_view, name="clientlogoupload"),
    path('approveview/', views.approve_view, name="approveview"),
    path('approveimage/', views.approveimage_view, name="approveimage"),
    path('approvedimage/<int:id>/', views.approvedimage_view, name="approvedimage"),
    path('approvelogo/', views.approvelogo_view, name="approvelogo"),
    path('approvedlogo/<int:id>/', views.approvedlogo_view, name="approvedlogo"),
    path('approvequestionans/', views.approvequestionans_view,
         name="approvequestionans"),
    path('approvedquestionans/<int:id>/',
         views.approvedquestionans_view, name="approvedquestionans"),

    path('approveassumptionrisk/', views.approveassumptionrisk_view,
         name="approveassumptionrisk"),
    path('approvedassumptionrisk/<int:id>/', views.approvedassumptionrisk_view,
         name="approvedassumptionrisk"),
    path('disapprovedimage_view/<int:id>/',
         views.disapprovedimage_view, name="disapprovedimage"),
    path('disapprovedlogo_view/<int:id>/',
         views.disapprovedlogo_view, name="disapprovedlogo"),
    path('disapproveassumptionrisk/<int:id>/',
         views.disapprovedassumptionrisk_view, name="disapprovedassumptionrisk"),
    path('disapprovequestionans/<int:id>/',
         views.disapprovequestionans_view, name="disapprovequestionans"),
    #path('UserQuestion/', views.notsatisfieddoc_view, name="UserQuestion"),
    # path('DownloadPicAndImages/', views.DownloadPicAndImages,
    #      name="DownloadPicAndImages"),

    #path('selected2/', include('RFP.urls')),
    path('user/<str:id>/', views.user_upload_question_view, name="UP"),
    path('userlogin/', views.userlogin_view, name="userlogin"),
    path('userstandardsection/', views.userstandardsection_view,
         name="userstandardsection"),
    path('userquestionans/', views.userquestionans_view, name="userquestionans"),
    path('useraddextraimages/', views.useraddextraimages_view,
         name="useraddextraimages"),
    path('userriskandassumption/', views.userriskandassumption_view,
         name="userriskandassumption"),
    #     path('userquestionanssavedata/', views.userquestionanssavedata_view,
    #          name="userquestionanssavedata"),
    path('userstandardsectiondata/', views.userstandardsection_view,
         name="userstandardsectiondata"),
    path('useraddlogo/', views.useraddlogo_view,
         name="useraddlogo"),
    path('usersummerytable/', views.usersummerytable_view,
         name="usersummerytable"),
    path('rejectfeedbackform/<int:id>/', views.rejectfeedbackform_view,
         name="rejectfeedbackform"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
