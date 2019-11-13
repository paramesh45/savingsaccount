from django.shortcuts import render
from .models import SavimgsAccountmodel

# Create your views here.
def showindex(request):
    auto_no = 0
    try:
        res = SavimgsAccountmodel.objects.all()[::-1][0]
        auto_no = int(res.acno) + 1
    except IndexError:
        auto_no=10000006000



    return render(request,"index.html",{"acno":auto_no})


def saveaccount(request):
    acno=request.POST.get("acno")
    name=request.POST.get("name")
    type=request.POST.get("acctype")
    age=request.POST.get("age")
    gender=request.POST.get("s1")
    o_bal=request.POST.get("open_bal")
    im=request.FILES["image"]
    SavimgsAccountmodel(acno=acno,name=name,type=type,age=age,gender=gender,o_bal=o_bal,photo=im).save()
    data=SavimgsAccountmodel.objects.all()
    res = SavimgsAccountmodel.objects.all()[::-1][0]
    auto_no = int(res.acno) + 1

    return render(request,"index.html",{"data":data,'acno':auto_no})






