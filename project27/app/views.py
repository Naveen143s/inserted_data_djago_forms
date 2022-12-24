from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_data(request):
    forms=SchoolForms()
    d={'forms':forms}
    if request.method=='POST':
        form_data=SchoolForms(request.POST)
        if form_data.is_valid():
            n=form_data.cleaned_data['name']
            p=form_data.cleaned_data['principal']
            l=form_data.cleaned_data['location']
            OBJ=school.objects.get_or_create(name=n,principal=p,location=l)[0]
            OBJ.save()
            return HttpResponse('data inserted sucessfully')

        
    return render(request,'insert_data.html',d)
