from django.db import models
from redactor.fields import RedactorField

# Create your models here.
class KategoriArtikel(models.Model):
    kategori = models.CharField(max_length=200)

    def __str__(self):
        return self.kategori

class Artikel(models.Model):
    judul = models.CharField(max_length=300)
    gambar = models.FileField(upload_to='static/artikel/gambar/')
    tanggal = models.DateField()
    kategori = models.ForeignKey(KategoriArtikel, on_delete=models.CASCADE)
    isi = RedactorField(
        verbose_name=u'',
        redactor_options={
            'lang': 'en',
            'focus': 'true',
            'overlay': 'false',
        },
    )

    def __str__(self):
        return self.judul




class Berita(models.Model):
    judul = models.CharField(max_length=300)
    gambar = models.FileField(upload_to='static/berita/gambar/')
    tanggal = models.DateField()
    isi = RedactorField(
        verbose_name=u'',
        redactor_options={
            'lang': 'en',
            'focus': 'true',
            'overlay': 'false',
        },
    )

    def __str__(self):
        return self.judul

class Event(models.Model):
    judul = models.CharField(max_length=300)
    gambar = models.FileField(upload_to='static/event/gambar/')
    tanggal = models.DateField()
    isi = RedactorField(
        verbose_name=u'',
        redactor_options={
            'lang': 'en',
            'focus': 'true',
            'overlay': 'false',
        },
    )

    def __str__(self):
        return self.judul

class TesPost(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()