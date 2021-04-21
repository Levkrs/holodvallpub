from django.db import models

# Create your models here.
class Datatable(models.Model):
    imei = models.BigIntegerField()
    val0 = models.CharField(max_length=50, blank=True, null=True)
    val1 = models.CharField(max_length=20)
    val2 = models.CharField(max_length=20)
    val3 = models.CharField(max_length=20)
    val4 = models.CharField(max_length=20)
    val5 = models.CharField(max_length=20)
    val6 = models.CharField(max_length=20)
    val7 = models.CharField(max_length=20)
    val8 = models.CharField(max_length=20)
    val9 = models.CharField(max_length=20)
    val10 = models.CharField(max_length=20)
    val11 = models.CharField(max_length=20)
    val12 = models.CharField(max_length=20)
    val13 = models.CharField(max_length=20)
    val14 = models.CharField(max_length=20)
    val15 = models.CharField(max_length=20)
    val16 = models.CharField(max_length=20)
    val17 = models.CharField(max_length=20)
    val18 = models.CharField(max_length=20)
    val19 = models.CharField(max_length=20)
    val20 = models.CharField(max_length=20)
    val21 = models.CharField(max_length=20)
    val22 = models.CharField(max_length=20)
    val23 = models.CharField(max_length=20)
    val24 = models.CharField(max_length=20)
    val25 = models.CharField(max_length=20)
    val26 = models.CharField(max_length=20)
    val27 = models.CharField(max_length=20)
    val28 = models.CharField(max_length=20)
    val29 = models.CharField(max_length=20)
    val30 = models.CharField(max_length=20)
    val31 = models.CharField(max_length=20)
    val32 = models.CharField(max_length=20)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dataTable'
