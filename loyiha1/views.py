from django.shortcuts import render
from .models import Blog,Position, Users
def base(request):

    return render(request,'hello.html')


def page1(request):
    a=Blog.objects.all()
    return render(request, 'page/page.html',{'salom':a})


def people(request):
    a=3
    us=Users.objects.all()
    pos=Position.objects.all()
    talab=Users.objects.filter(position_id=2)
    oqituchi=Users.objects.filter(position_id=1)

    return render(request, 'users.html',{'user':us,'oqtuvchi':oqituchi,'talaba':talab})
# Create your views here.
