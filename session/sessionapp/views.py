from django.shortcuts import render
from django.http import HttpResponse

# def input(request):

#     return render(request,'base.html')

def add(request):
    # if request.method=='GET':
    #     x=int(request.POST.get('f'))
    #     y=int(request.POST.get('s'))
        # z=x+y
        z="vaasu"
        res=HttpResponse('Values submitted successfully')

        res.set_cookie('mahesh',z)

        return res
# def display(request):

#     for a,b in request.COOKIES.items():
#         print(a,b)

#     if 'z' in request.COOKIES:
#         a=request.COOKIES['z']
#         return HttpResponse('addition of two numbers :'+a)
#     else:
#         return render(request,'base.html')

# Create your views here.
