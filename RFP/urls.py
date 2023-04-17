from RFP import views
from django.urls import path

urlpatterns = [
     # path('index/',views.index_view,name="index"), #first page {% url 'index'%}
     path('details/', views.infodetails_view,
          name="details"),  # second page details
     # third page select standard RFP {% url 'load'%}
     path('content', views.doc_content_view, name="content"),
     # fourth page type question RFP {% url 'firstpage'%}
     path('page/', views.firstpage_view, name="firstpage"),
     # fifth page mcq options {% url 'secondpage'%}
     path('pages/', views.secondpage_view, name="secondpage"),
     # sixth page preview {% url 'preview'%}
     path('ews/', views.pre_view, name="preview"),
     # preview page print standard pdf {% url 'download'%}
     path('download/', views.printpdf, name="download"),
     # preview page print standard pdf {% url 'download'%}
     path('download_uploaded/', views.drop_print_pdf, name="download_uploaded"),
     # preview page erase data and again start RFP {% url 'newrfp'%}
     path('newrfp/', views.start_new_rfp, name="newrfp"),
     # path('load/',views.printpdf1,name="load"),#type question page print standard pdf {% url 'load'%}
     # path('file/',views.download,name="down"),{% url 'down file' %}
     path('picup/', views.pic_upload_view, name="picup"),  # {% url 'picup' %}
     # {% url 'picup' %}file_injection
     path('picdown/', views.pic_down_view, name="picdown"),
     path('documentapproval/', views.documentapproval_view, name="documentapproval"),
     path('injection/', views.file_injection_view, name="file_injection"),
     path('rfp/', views.drop_rfp_view, name="droprfp"),
     path('ques1/', views.drop_rfpquest_view1, name="ques1"),
     path('ques2/<int:id>/', views.drop_rfpquest_view2, name="ques2"),

     path('drp/', views.drop_rfp_preview_view, name="drp"),
     path('request/', views.approve_view, name="approve"),
     path('confirm/<int:id>/', views.confirm_view, name="confirm"),
     path('ar/<int:id>/', views.approved_view, name="ar"),
     path('dr/<int:id>/', views.disapproved_view, name="dr"),
     path('file/', views.Binaryfile_view, name="Binaryfile"),
     path('add/', views.geoadd_view, name="geoadd"),
     path('gpt/', views.chatgpt_view, name="chatgpt"),
     path('index/', views.SelectedIndex_view, name="SelectedIndex"),
     path('index/<int:id>/', views.SelectedIndex2_view, name="SelectedIndex2"),
     path('mcq/<int:id>/', views.Onscreenmcq_view, name="Onscreenmcq"),
     path('SelectedIndexlastPage/', views.SelectedIndexlastPage_view,
          name="SelectedIndexlastPage"),
     path('rfp-document/', views.generate_rfp_document, name="GenerateRfpDoc"),

    # path('userquestion/<int:id>/',views.user_upload_question_view,name="UP"),

]
