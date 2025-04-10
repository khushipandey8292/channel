from django.shortcuts import render
def index(request,group_name):
    return render(request,'home.html',{'groupname':group_name})

