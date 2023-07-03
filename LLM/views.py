from django.shortcuts import render
from DataHandler.api.views import processed_data

def view(request):
    return render(request, 'LLM/test.html')

