from django.shortcuts import render
from app.forms import *
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


class cbv_register(View):
    def get(self, request):
        EUFO = UserForm()
        EPFO = ProfileForm()
        d = {'EUFO':EUFO, 'EPFO':EPFO}
        return render(request, 'cbv_register.html', d)
    

    def post(self, request):
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponse('Done..')
        return HttpResponse('Invalid Data')
