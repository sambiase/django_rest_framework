from django.shortcuts import render

def mainpage (request):
    return render(request,template_name='index.html')