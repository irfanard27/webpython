from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from blog.models import Artikel

def ajax_artikel_count(request):
    return JsonResponse({'count': Artikel.objects.count()})

def ajax_artikel_all(request):
    data = serializers.serialize("json", Artikel.objects.all())
    return HttpResponse(data, content_type='applications/json')
