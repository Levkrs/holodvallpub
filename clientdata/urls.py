from django.contrib import admin
from django.urls import path, include

import clientdata.views as clientdata

app_name = 'clientdata'

urlpatterns = [
    path('', clientdata.listDevice, name='listdevice'),
    path('registerdevice/', clientdata.registerDevice, name='registerdevice'),
    path('deviceprofile/<int:imei>/', clientdata.updateDevice, name='updatedevice'),
    path('deletedevice/<int:imei>/', clientdata.deleteDevice, name='deleteDevice'),
    path('table/<int:imei>/', clientdata.tableDataView, name='tableDataView'),
    path('charts/', clientdata.charts, name='cahrtsDataView'),
    path('chartstest/', clientdata.testcahrts, name='chartsTest'),
    path('test/', clientdata.TestListView.as_view(), name='test'),
]
