from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    context={}
    context['hello']="Hello World"
    return render(request,'home.html',context)


def addMembers(request):
    form=AddMembersForm()
    if request.method=='POST':
        form=AddMembersForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context={
        'form':form
    }
    return render(request,'addMember.html',context)



def membersDetails(request):
    member=AddMembers.objects.all()
    if request.method=="GET":

        title=request.GET.get('member_name')
        pay=request.GET.get('select')
        if title!=None:
            member=AddMembers.objects.filter(fullName__icontains=title)
        if pay!=None:
            member=AddMembers.objects.filter(paid=pay)

    context={
        'members':member
    }
    
    return render(request,'allMembers.html',context)


def deleteDetail(request,pk):
    obj=AddMembers.objects.get(mobile=pk)
    if obj!=None:
        obj.delete()
        return redirect('home')
    return render(request,'allMembers.html')


