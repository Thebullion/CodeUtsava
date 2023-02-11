from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'login_hospital.html')
    else:
        return render(request, 'login.html')

def Agencylog(request):

    return render(request,'loginAgency.html')