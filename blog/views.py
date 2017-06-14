
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def demo(request):
	return TemplateResponse(request, 'demo.html')
