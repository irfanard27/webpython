from django.contrib import admin
from .models import *
from .forms import ArtikelAdminForm, BeritaAdminForm
# Register your models here.


class ArtikelAdmin(admin.ModelAdmin):

    def gambar_tag(self, obj):
        return u'<img src="/%s" width="200" height="auto"/>' % obj.gambar.url

    gambar_tag.allow_tags = True

    list_display = ('judul', 'kategori')
    list_filter = ('judul', 'tanggal', 'kategori')
    search_fields = ['judul']
    form = ArtikelAdminForm

class BeritaAdmin(admin.ModelAdmin):

    list_display = ('judul', 'tanggal')
    list_filter = ('judul', 'tanggal')

    form = BeritaAdminForm

class EventAdmin(admin.ModelAdmin):

    list_display = ('judul', 'tanggal')
    list_filter = ('judul', 'tanggal')


admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(KategoriArtikel)
admin.site.register(Berita, BeritaAdmin)
admin.site.register(Event, EventAdmin)
