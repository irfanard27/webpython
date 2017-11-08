from django.db import models

# Create your models here.
class Organisasi(models.Model):
    nama_organisasi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_organisasi

class Departemen(models.Model):
    nama_departemen = models.CharField(max_length=100)
    organisasi = models.ForeignKey(Organisasi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_departemen

class Pelajar(models.Model):
    JENIS = (('laki-laki', 'laki-laki'),
             ('perempuan', 'perempuan'))
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=100, choices=JENIS)
    foto = models.FileField(upload_to='static/pelajar/foto')
    departemen = models.ForeignKey(Departemen, on_delete=models.CASCADE)


    def __str__(self):
        return self.nama_lengkap