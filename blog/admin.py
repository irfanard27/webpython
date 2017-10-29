from django.contrib import admin
from .models import *
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul','tanggal','kategori','gambar')

class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')

admin.site.register(Artikel,ArtikelAdmin)
admin.site.register(KategoriArtikel)
admin.site.register(Berita, BeritaAdmin)
