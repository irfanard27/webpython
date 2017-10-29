from django.db import models

# Create your models here.
class KategoriArtikel(models.Model):
    kategori = models.CharField(max_length=200)

    def __str__(self):
        return self.kategori

class Artikel(models.Model):
    judul = models.CharField(max_length=300)
    isi = models.TextField()
    gambar = models.FileField(upload_to='static/blog/gambar/')
    tanggal = models.DateField()
    kategori = models.ForeignKey(KategoriArtikel, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul

    def image_tag(self):
        return u'<img src="%s" />' % 'static/blog/gambar/' % self.gambar


class Berita(models.Model):
    judul = models.CharField(max_length=300)
    gambar = models.FileField(upload_to='static/berita/gambar/')
    tanggal = models.DateField()
    isi = models.TextField()

    def __str__(self):
        return self.judul
