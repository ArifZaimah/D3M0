
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def dashboard(request):
    context = {
        "user_count" : 42,
        "sales" : 999.99,
    }
    return render(request, "dashboard/index.html", context)

def home(request):
    return redirect('dashboard')  # uses the name='dashboard' in urls.py
"""
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/index.html')
"""
