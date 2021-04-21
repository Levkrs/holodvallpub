from django.contrib import admin
from clientdata.models import ClientListDevice, NameValueClientDevice

admin.site.register(NameValueClientDevice)
admin.site.register(ClientListDevice)

# Register your models here.
