from django.shortcuts import render

# Create your views here.

def testBase(response):
    return render(response, 'main/base.html', {})

def testId(response, id):
    return render(response, 'register/test_id.html', {'id':id})