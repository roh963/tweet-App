from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, world. You're at the polls Home.")
    return render(request, 'web/index.html')

