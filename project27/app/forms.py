from django import forms


class SchoolForms(forms.Form):
    name=forms.CharField(max_length=100)
    principal=forms.CharField(max_length=100)
    location=forms.CharField(max_length=100)