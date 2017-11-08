from django.contrib import admin
from .models import *
from django import forms

# Register your models here.
class PelajarAdminForm(admin.ModelAdmin):
    JENIS = (('laki-laki', 'laki-laki'),
        ('perempuan', 'perempuan'))

    jenis_kelamin = forms.ChoiceField(choices=JENIS)

class PelajarAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'alamat', 'jenis_kelamin', 'tanggal_lahir',)
    forms = PelajarAdminForm


class DepartemenAdmin(admin.ModelAdmin):

    list_display = ('nama_departemen','organisasi')
    list_filter = ['organisasi']

admin.site.register(Pelajar, PelajarAdmin)
admin.site.register(Departemen, DepartemenAdmin)
admin.site.register(Organisasi)