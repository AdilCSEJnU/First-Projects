from django.shortcuts import render, HttpResponse
from tution.models import Contact
def home(request):
    name=['Ahad','Adil']
    context={
        'name':name,
    }
    return render(request, 'home.html',context)

