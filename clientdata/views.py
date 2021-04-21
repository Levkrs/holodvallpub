import json

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from icecream import ic

from clientdata.forms import ClientAddDeviceForm, ClientUpdateDeviceForm
from django.urls import reverse
from clientdata.models import ClientListDevice, NameValueClientDevice
from valdevice.models import Datatable
import re
from clientdata.forms import DataInputForm
# from datetime import datetime
# import paho.mqtt.client as mqtt
# from threading import Thread
# from icecream import ic

@login_required()
def registerDevice(request):
    if request.method == 'POST':
        print('POST')
        form = ClientAddDeviceForm(request.POST, request.FILES,
                                   initial={'user': request.user})
        if form.is_valid():
            form.save()
            device = ClientListDevice(imei=request.POST['imei'])
            device2 = NameValueClientDevice(imei_device=device)
            device2.save()
            print(device2)
            return HttpResponseRedirect(reverse('clientdata:listdevice'))
    else:
        form = ClientAddDeviceForm(initial={'user': request.user})
    context = {
        'form': form,

    }
    return render(request, 'clientdata/addclientdevice.html', context)

@login_required()
def listDevice(request):
    device = ClientListDevice.objects.filter(user=request.user)
    # form = ClientListDeviceForm(instance=request.user)

    context = {
        # 'form': form,
        'device': device
    }
    return render(request, 'clientdata/clientlistdevice.html', context)

@login_required()
def deleteDevice(request, imei):
    device = get_object_or_404(ClientListDevice, imei=imei)
    print(device)
    device.delete()
    return HttpResponseRedirect(reverse('clientdata:listdevice'))

@login_required()
def updateDevice(request, imei):
    device = NameValueClientDevice.objects.get(imei_device=imei)
    if request.method == 'POST':
        form = ClientUpdateDeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ClientUpdateDeviceForm(instance=device)
    context = {
        'imei': imei,
        'form': form
    }
    return render(request, 'clientdata/deviceprofile.html', context)

@login_required()
def tableDataView(request, imei):
    """
        # MQTT потоками на сервер

        def on_message(client, userdata, msg):
            # print("Data requested " + str(msg.payload))
            ic(msg.payload)


        def on_connect(client, userdata, flags, rc):
            print('Connect from user ')
            client.subscribe("#")

        def subscribing(client):
            client.on_message = on_message
            client.loop_start()
            print(client)


        def main():
            client = mqtt.Client(transport="websockets")
            client.username_pw_set("admin", "lev6410200")
            client.connect("192.168.0.113", 9001, 60)
            client.on_connect = on_connect
            sub = Thread(target=subscribing, args=(client,))
            sub.start()
        main()
    """

    if request.method == 'POST':
        form = DataInputForm(data=request.POST)
        if form.is_valid():
            print('Valid')
            start_time = request.POST['date_val_start']
            end_time = request.POST['date_val_end']
            print('Start_stop date')
            nameVal = NameValueClientDevice.objects.filter(imei_device=imei)
            print(nameVal.count())
            if nameVal.count() > 0:
                dictName = nameVal[0].__dict__
                nameTableRow = []
                valTableRow = []
                for item in dictName:
                    if re.match(r'val\d+$', item):
                        if dictName[item + '_check_view']:
                            valTableRow.append(item)
                            nameTableRow.append(dictName[item])
                valTableRow.append('date')
                dataDevice = Datatable.objects.filter(imei=imei).filter(date__range=[start_time, end_time]).values_list(
                    *valTableRow)
                if dataDevice.count() > 0:
                    print(dataDevice[0].__dict__)
                    print(' > 0 ')
                else:
                    print(' < 0 ')
                nameTableRow.append('Дата')

    else:
        form = DataInputForm()
        nameVal = NameValueClientDevice.objects.filter(imei_device=imei)
        ic(nameVal)
        dictName = nameVal[0].__dict__
        # print(dictName.keys())
        nameTableRow = []
        valTableRow = []
        for item in dictName:
            if re.match(r'val\d+$', item):
                if dictName[item + '_check_view']:
                    valTableRow.append(item)
                    nameTableRow.append(dictName[item])
        valTableRow.append('date')
        dataDevice = Datatable.objects.filter(imei=imei).order_by('-id')[0:100].values_list(*valTableRow)
        nameTableRow.append('Дата')
        print(imei)
        # print(valTableRow)
        # print(nameTableRow)
        # if dataDevice[0]:
        #     item = dataDevice[0]
        #     print(item[0])

        # print(dataDevice[0])
    # testdata = Datatable.objects.filter(imei=865472035729859).\
    #     filter(date__range=('2020-7-20', '2020-7-21'))[:100]
    # print(testdata.__dict__)
    # for items in testdata:
    #     print(items.__dict__)

    # nameTableRow.append('Дата')
    ic(valTableRow)
    context = {
        'rowname': nameTableRow,
        'valname': valTableRow,
        'device': dataDevice,
        'imei': imei,
        'form': form,
        'username_mqtt': 'device',
        'password_mqtt': 'device',
        'valname':valTableRow

    }
    return render(request, 'clientdata/tabledata.html', context)


def charts(request):
    month = ["month1", "month2", "month3"]
    dataVal = [100, 200, 1400]
    dataVal1 = [10, 15, 134]

    context = {
        'monthData': month,
        'dataVal': dataVal,
        'dataVal1': dataVal1
    }
    return render(request, 'clientdata/chartsdata.html', context)


def testcahrts(request):
    if request.method == 'POST':
        form = DataInputForm(data=request.POST)
        if form.is_valid():
            print('Valid')
            start_time = request.POST['date_val_start']
            end_time = request.POST['date_val_end']
            object_range_data = Datatable.objects.filter(imei=863584031193955).filter(
                date__range=[start_time, end_time])
            print(object_range_data.count())
    else:
        object_range_data = []
    nameVal = NameValueClientDevice.objects.filter(imei_device=863584031193955)
    dictName = nameVal[0].__dict__
    nameTableRow = []
    for item in dictName:
        if re.match(r'val\d+$', item):
            if dictName[item + '_check_view']:
                nameTableRow.append(dictName[item].lower())

    # dataObject = Datatable.objects.filter(imei=863584031193955)[:5]

    dataObject = object_range_data
    if object_range_data:
        # dataObject1 = dataObject.values()[:5]
        dataObject1 = dataObject.values()[:5]
        # dataObject1 = Datatable.objects.filter(imei=863584031193955).values()[:5]
        dataObject1 = list(dataObject1)
        dataJson = json.dumps(dataObject1, cls=DjangoJSONEncoder)
        values_val0 = list(map(lambda x: x.val4, dataObject))
        date_val = list(map(lambda x: (x.date).strftime('%m.%d.%Y | %H:%M:%S'), dataObject))
    else:
        values_val0 = []
        date_val = []
        dataJson = []
        nameTableRow = []
        form = DataInputForm()
    context = {
        'values_val0': values_val0,
        'date_val': date_val,
        'test_val': dataJson,
        'name_val': nameTableRow,
        'form': form,
    }
    return render(request, 'clientdata/chartstest.html', context)


class TestListView(ListView):
    # paginate_by = 1
    model = ClientListDevice

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestListView, self).get_context_data(**kwargs)
        # print(context['object_list'])
        # ic(context)
        return context

    # def get_queryset(self):
    #     query = super().get_queryset()
    #     ic(query)
    #     return query
    # def get_context_object_name(self, object_list):
    #     object_content = super(TestListView, self).get_context_object_name(object_list)
    #     ic(object_content)
    #     return object_content

    def dispatch(self, request, *args, **kwargs):
        disp = super(TestListView, self).dispatch(request, *args, **kwargs)
        ic(disp)
        return disp