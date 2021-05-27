from django.shortcuts import render
from django.http import HttpResponse
from .models import*

def CommonData(request):
    cat=Category.objects.all()
    subcat=SubCategory.objects.all()
    return{"cat":cat,"subcat":subcat}
    
    

def Home(request):
    d={"title":"FashionHub"}
    d.update(CommonData(request))
    print(d)
    return render(request,'index.html',d)

def About(request):
     d={"title":"FashionHub:About"}
     d.update(CommonData(request))
     print(d)
     return render(request,'about.html',d)

def Contact(request):
    if 'contactForm' in request.POST:
        n=request.POST['name']
        e=request.POST['email']
        m=request.POST['msg']
        ContactForm.objects.create(name=n,email=e,msg=m)
    d={"title":"FashionHub:Contact"}
    d.update(CommonData(request))
    print(d)
    return render(request,'contact.html',d)
    
