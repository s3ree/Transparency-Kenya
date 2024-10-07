from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/index.html')

def spending_tracker(request):
    return render(request, 'core/spending-tracker.html')

def policy_impact(request):
    return render(request, 'core/policy-impact.html')

def about(request):
    return render(request, 'core/about.html')
