from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Reg


from .forms import RegForm,LoginForm
class Home(View):
    def get(self,request):
        form = RegForm()
        return render(request,template_name="home.html",context={"form":form})

class Reginput(View):
    def get(self,request):
        con_dic={"regform":RegForm}
        return render(request,template_name="reginput.html",context=con_dic)
class Regview(View):
    def get(self,request):
        rf = RegForm(request.POST)
        if rf.is_valid():
            rf.save()
            return HttpResponse("success")
class Loginput(View):
    def get(self,request):
        con_dic= {"loginform": LoginForm()}
        return render(request,template_name="login.html",context=con_dic)
class loginview(View):
    def post(self,request):
        lf = LoginForm(request.POST)
        if lf.is_valid():
            res=Reg.objects.filter(username=lf.cleaned_data["username"],
                                   password=lf.cleaned_data["password"])
            if res:
                return HttpResponse(" login success")
            else:
                return HttpResponse(" login failed")
