from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'user_name': 'Akhil','age':22}
    return render(request,'data_render.html',context=d)
