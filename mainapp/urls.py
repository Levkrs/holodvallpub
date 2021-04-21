
from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('posts/', mainapp.post_from_db, name='POST'),
    path('api_req/imei/<str:token>/', mainapp.api_get_imei, name='api_get_imei'),
    path('api_req/valname/<int:imei>/', mainapp.api_get_valname, name='api_get_valname')
    # #path('tables/', mainapp.tables, name='tables'),
    # path('tables/', mainapp.TableList.as_view(), name='tables'),
    # path('charts/', mainapp.charts, name='charts'),
    # #path('device/', mainapp.devicelist, name='device'),
    # #path('device/<int:page>', mainapp.devicelist, name='device_pagination'),
    # path('device/', mainapp.DeviceList.as_view(), name='device'),
    # path('holod/', mainapp.holod, name='holod'),
    # path('fire/', mainapp.fire, name='fire'),
    # path('create/', mainapp.CreateDevice.as_view(), name='create'),



]
