from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django import forms
from django.forms import fields
# Create your views here.

class F1Form(forms.Form):
    user = forms.fields.CharField(
                                  max_length=18,
                                  min_length=6,
                                  required=True,
                                  error_messages={"max_length":"too long","min_length":"too short","required":"is not empty"}
                                  )
    pwd  = forms.fields.CharField(
                                  required=True,
                                  min_length=8,
                                  error_messages={"required":"is not empty","min_length":"too short"}
                                  )
    age = forms.fields.IntegerField(
                                    required=True,
                                    error_messages={"required":"is not empty","invalid":"格式错误"}
                                    )
    email = forms.fields.EmailField(
                                    required=True,
                                    min_length=8,
                                    error_messages={"required":"is not empty","min_length":"too short","invalid":"格式错误"}
                                    )

def fm(request):
    if request.method=="GET":
        obj = F1Form()
        return render(request,"form02.html",{"obj":obj})
    if request.method == "POST":
    # else:
        obj = F1Form(request.POST)
        if obj.is_valid():
            print("OK",obj.cleaned_data)
            return redirect("https://www.youtube.com")
        else:
            print("error",obj.errors)
            return render(request,"form02.html",{"obj":obj})
