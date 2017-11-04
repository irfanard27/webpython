from django.contrib import admin
from .models import *
from django import forms
from redactor.widgets import RedactorEditor

# Register your models here.
class ArtikelAdminForm(forms.ModelForm):
    class Meta:
        model = Artikel
        widgets = {
           'isi': RedactorEditor(redactor_options={
               'minHeight': '400px',
               'overlay': False,
               'autoformat' : True
           }),
        }
        fields = ('judul', 'kategori', 'tanggal', 'gambar','isi')


class ArtikelAdmin(admin.ModelAdmin):

    def gambar_tag(self, obj):
        return u'<img src="/%s" width="200" height="auto"/>' % obj.gambar.url

    gambar_tag.allow_tags = True

    list_display = ('judul', 'kategori', 'gambar_tag')
    list_filter = ('judul', 'tanggal', 'kategori')
    form = ArtikelAdminForm


class BeritaAdminForm(forms.ModelForm):
    class Meta:
        model = Artikel

        widgets = {

           'judul': forms.TextInput(attrs={
               'style': 'width:100%',
               'placeholder' : 'Judul',
           }),

           'isi': RedactorEditor(redactor_options={
               'minHeight': '400px',
               'overlay': False,
               'autoformat' : True
           }),
        }

        fields = ('judul', 'gambar', 'tanggal','isi')


class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    list_filter = ('judul', 'tanggal')
    form = BeritaAdminForm

class EventAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    list_filter = ('judul', 'tanggal')


admin.site.register(Artikel,ArtikelAdmin)
admin.site.register(KategoriArtikel)
admin.site.register(Berita, BeritaAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TesPost)
