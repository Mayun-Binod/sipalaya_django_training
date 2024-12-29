from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=='POST':
        data=request.POST
        
        nm=data['name'] #sujan
        age=data['age']#88
        email=data['email']#sujan@gmail.com
        message=data['message']#hello
        dob=data['dob']
        
        user=Student(name=nm,age=age,email=email,message=message,dob=dob)
        user.save()
        return HttpResponse("submit!!!")
        
    return render(request,'home.html')

def show(request):
  
    # data=Student.objects.all()
    # data=Student.objects.filter(name="Binod",age=22)
    # data=Student.objects.exclude(name="sujan")
    # data=Student.objects.order_by('age')
    # data=Student.objects.order_by('-age')
    # data=Student.objects.order_by('?')[:3]
    # data=Student.objects.values('name','age')
    


    # data=Student.objects.get(id=3)
    # data=Student.objects.first()
    # data=Student.objects.last()
    # data=Student.objects.latest('name')
    # data=Student.objects.earliest('name')
    
    # Student.objects.create(name="hari",age=55,email="hari@gmail.com",message="hello")
    # Student.objects.filter(id=8).update(name="hari update")
    # Student.objects.get(id=8).delete()
    
    
    #lookup
    # data=Student.objects.filter(name__exact='sujan')
    # data=Student.objects.filter(name__iexact='sujan')
    # data=Student.objects.filter(name__icontains="an")
    # data=Student.objects.filter(name__endswith="an")
    # data=Student.objects.filter(name__startswith="s")
    # data=Student.objects.filter(age__lt=30)
    # data=Student.objects.filter(age__lte=30)
    # data=Student.objects.filter(age__gt=30)
    # data=Student.objects.filter(age__gte=30)
    # data=Student.objects.filter(age__range=(30,60))
    
    started_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')
    
    if started_date and end_date:
        data=Student.objects.filter(dob__range=(started_date,end_date))
    else:
        data=Student.objects.all()



    return render(request,'show.html',{'data':data})




""" searched=request.GET.get('searched') 
    if searched:
        data=Student.objects.filter(name__icontains=searched)
    else:
        data=Student.objects.all() #query set"""
    # return render(request,'show.html',{'data':data})