from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Artikel, Berita , KategoriArtikel
# Create your views here.

def index(request):
    artikel = Artikel.objects.all()[:4]
    berita = Berita.objects.all()[:6]
    context = {
        'artikels': artikel,
        'beritas': berita
    }
    return render(request, 'web/index.html', context)

def artikel(request):
    artikel = Artikel.objects.all().order_by('-id')[:6]
    kategoris = KategoriArtikel.objects.annotate(num_artikel=Count('artikel'))
    context = {
        'artikels': artikel,
        'kategoris': kategoris
    }
    return render(request, 'web/blog.html', context)

def artikel_view(request,id):
    artikel = Artikel.objects.get(pk=id)
    artikel_all = Artikel.objects.all()[:3]
    context = {
        'artikel': artikel,
        'berita_all':artikel_all
    }
    return render(request, 'web/artikel-view.html', context)

def berita(request):
    berita = Berita.objects.all()
    context = {
        'beritas': berita,
    }
    return render(request, 'web/berita.html', context)

def berita_view(request,id):
    berita = Berita.objects.get(pk=id)
    berita_all = Berita.objects.all()[:3]
    context = {
        'berita': berita,
        'berita_all':berita_all
    }
    return render(request, 'web/berita-view.html', context)