from django.shortcuts import render , HttpResponse
from .models import Contact,Post
from .forms import ContactForm, PostForm

# Create your views here.
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            form.save()
    else:
        form=ContactForm()

    return render(request, 'contact.html',{'form':form})
def postview(request):
    post=Post.objects.all()
    return render(request, 'tution/postview.html',{'post':post})
def postcreat(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")
    else:
        form=PostForm()
    return render (request,'tution/postcreat.html',{'form':form})