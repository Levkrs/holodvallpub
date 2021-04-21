from django.db import models
from authapp.models import ValAuth
from valdevice.models import Datatable

# Create your models here.

class ClientListDevice(models.Model):
    user = models.ForeignKey(ValAuth, on_delete=models.CASCADE, related_name='clientlistdevice')
    imei = models.BigIntegerField(unique=True, primary_key=True)
    address = models.CharField(max_length=200, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True)


class NameValueClientDevice(models.Model):
    imei_device = models.ForeignKey(ClientListDevice, on_delete=models.CASCADE)
    val0 = models.CharField(max_length=50, blank=True, null=True, default='Val0')
    val1 = models.CharField(max_length=50, blank=True, null=True, default='Val1')
    val2 = models.CharField(max_length=50, blank=True, null=True, default='Val2')
    val3 = models.CharField(max_length=50, blank=True, null=True, default='Val3')
    val4 = models.CharField(max_length=50, blank=True, null=True, default='Val4')
    val5 = models.CharField(max_length=50, blank=True, null=True, default='Val5')
    val6 = models.CharField(max_length=50, blank=True, null=True, default='Val6')
    val7 = models.CharField(max_length=50, blank=True, null=True, default='Val7')
    val8 = models.CharField(max_length=50, blank=True, null=True, default='Val8')
    val9 = models.CharField(max_length=50, blank=True, null=True, default='Val9')
    val10 = models.CharField(max_length=50, blank=True, null=True, default='Val10')
    val11 = models.CharField(max_length=50, blank=True, null=True, default='Val11')
    val12 = models.CharField(max_length=50, blank=True, null=True, default='Val12')
    val13 = models.CharField(max_length=50, blank=True, null=True, default='Val13')
    val14 = models.CharField(max_length=50, blank=True, null=True, default='Val14')
    val15 = models.CharField(max_length=50, blank=True, null=True, default='Val15')
    val16 = models.CharField(max_length=50, blank=True, null=True, default='Val16')
    val17 = models.CharField(max_length=50, blank=True, null=True, default='Val17')
    val18 = models.CharField(max_length=50, blank=True, null=True, default='Val18')
    val19 = models.CharField(max_length=50, blank=True, null=True, default='Val19')
    val20 = models.CharField(max_length=50, blank=True, null=True, default='Val20')
    val21 = models.CharField(max_length=50, blank=True, null=True, default='Val21')
    val22 = models.CharField(max_length=50, blank=True, null=True, default='Val22')
    val23 = models.CharField(max_length=50, blank=True, null=True, default='Val23')
    val24 = models.CharField(max_length=50, blank=True, null=True, default='Val24')
    val25 = models.CharField(max_length=50, blank=True, null=True, default='Val25')
    val26 = models.CharField(max_length=50, blank=True, null=True, default='Val26')
    val27 = models.CharField(max_length=50, blank=True, null=True, default='Val27')
    val28 = models.CharField(max_length=50, blank=True, null=True, default='Val28')
    val29 = models.CharField(max_length=50, blank=True, null=True, default='Val29')
    val30 = models.CharField(max_length=50, blank=True, null=True, default='Val30')
    val31 = models.CharField(max_length=50, blank=True, null=True, default='Val31')
    val32 = models.CharField(max_length=50, blank=True, null=True, default='Val32')

    val0_check_view = models.BooleanField(default=True)
    val1_check_view = models.BooleanField(default=True)
    val2_check_view = models.BooleanField(default=True)
    val3_check_view = models.BooleanField(default=True)
    val4_check_view = models.BooleanField(default=True)
    val5_check_view = models.BooleanField(default=True)
    val6_check_view = models.BooleanField(default=False)
    val7_check_view = models.BooleanField(default=False)
    val8_check_view = models.BooleanField(default=False)
    val9_check_view = models.BooleanField(default=False)
    val10_check_view = models.BooleanField(default=False)
    val11_check_view = models.BooleanField(default=False)
    val12_check_view = models.BooleanField(default=False)
    val13_check_view = models.BooleanField(default=False)
    val14_check_view = models.BooleanField(default=False)
    val15_check_view = models.BooleanField(default=False)
    val16_check_view = models.BooleanField(default=False)
    val17_check_view = models.BooleanField(default=False)
    val18_check_view = models.BooleanField(default=False)
    val19_check_view = models.BooleanField(default=False)
    val20_check_view = models.BooleanField(default=False)
    val21_check_view = models.BooleanField(default=False)
    val22_check_view = models.BooleanField(default=False)
    val23_check_view = models.BooleanField(default=False)
    val24_check_view = models.BooleanField(default=False)
    val25_check_view = models.BooleanField(default=False)
    val26_check_view = models.BooleanField(default=False)
    val27_check_view = models.BooleanField(default=False)
    val28_check_view = models.BooleanField(default=False)
    val29_check_view = models.BooleanField(default=False)
    val30_check_view = models.BooleanField(default=False)
    val31_check_view = models.BooleanField(default=False)
    val32_check_view = models.BooleanField(default=False)
