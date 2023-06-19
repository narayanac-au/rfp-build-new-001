from .models import Image, DropQuery
from django import forms
from django.forms import ModelForm
from RFP.models import UserQuery, SelectDropQuery, info
from django_quill.forms import QuillFormField


class UserQueryForm(ModelForm):
    query = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = UserQuery

        fields = ['query', 'answer1', 'answer2', 'answer3']


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ["image"]


class SelectDropQueryForm(ModelForm):
    question = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SelectDropQuery

        fields = ['question', 'answer1', 'answer2', 'answer3']


class ProjectForm(forms.Form):
    body = QuillFormField()
# class UserQuestionForm(ModelForm):

#     class Meta:
#         model = UserQuestion

#         fields=['id','rfp_id','content_type','country','industry','Section','Sub_Section','question',]

#     widgets={
#         'Section':forms.TextInput(attrs={"class": "form-control"}),

#         'Sub_Section' :forms.TextInput(attrs={"class": "form-control"}),

#         'question' :forms.TextInput(attrs={"class": "form-control"})
#     }

# class InfoForm(ModelForm):
#     #question = forms.CharField( widget=forms.Textarea)

#     class Meta:
#         model = info

#         #fields = ['KPMGgeo', 'KPMGaddress']
