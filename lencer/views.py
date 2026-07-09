from django.shortcuts import render
from . models import datas
# Create your views here.
def home(request):
    pro=datas.objects.all()
    return render(request,'home.html',{'pr':pro})
    
