from .models import *
from django import forms
from redactor.widgets import RedactorEditor

class ArtikelAdminForm(forms.ModelForm):

    judul = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    kategori = forms.ModelChoiceField(queryset=KategoriArtikel.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    isi = forms.CharField(widget=RedactorEditor(redactor_options={
        'minHeight': '400px',
        'autoformat': True
    }))

    gambar = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    tanggal = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))

    class Meta:
        model = Artikel
        fields = ('judul', 'kategori','gambar', 'tanggal','isi')

class BeritaAdminForm(forms.ModelForm):

    judul = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Judul'
    }))

    isi = forms.CharField(widget=RedactorEditor(redactor_options={
        'minHeight': '400px',
        'autoformat': True
    }))

    gambar = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    tanggal = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))

    class Meta:
        model = Berita
        fields = ('judul', 'gambar', 'tanggal','isi')