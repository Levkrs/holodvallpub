from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from icecream import ic
import json

from authapp.models import ValAuth
from clientdata.models import NameValueClientDevice, ClientListDevice


@login_required()
def index(request):
    context = {
        # 'year': date.year,
        # 'device': device,
    }
    return render(request, 'mainapp/index.html', context)


@csrf_exempt
def post_from_db(request):
    val = settings.MQTT_VAL
    # val["1234"] = 133+1
    post_req = request.body
    json_val = json.loads(post_req)
    # ic(post_req)
    # if request == 'POST':
    # ic(json_val)
    # ic(json_val['test_val'])
    # ic(json_val.keys())
    for key in json_val:
        val[key] = json_val[key]

    # print("POST FORM DB")
    # print(settings.MQTT_VAL)
    ic(settings.MQTT_VAL)

    return HttpResponse(200)


def api_get_imei(request, token):
    test_token = '21c434df'
    token = token
    print(token)


    get_user_pk = ValAuth.objects.filter(unic_token=f'{test_token}').first()
    print(get_user_pk)
    # obj = NameValueClientDevice.objects.filter(imei_device=12323).values_list()
    # obj_json = serialize('json', NameValueClientDevice.objects.all())
    # imei_list_json = serialize('json', ClientListDevice.objects.values_list('pk'))
    imei_list_json = list(ClientListDevice.objects.values_list('pk').filter(user=get_user_pk))
    imei_list = list(map(lambda x: x[0], imei_list_json))
    json_imei_list = json.dumps(imei_list)
    # print(type(json_imei_list))

    return HttpResponse(json_imei_list, content_type="application/json")

def api_get_valname(requset, imei):
    # imei_test = 34897545
    imei=imei
    # test_token = '21c434df'
    # token=token
    # get_user_pk = ValAuth.objects.filter(unic_token=f'{test_token}').first()
    # valname = NameValueClientDevice.objects.filter(imei_device=imei).values_list()
    data = serializers.serialize('python',[NameValueClientDevice.objects.filter(imei_device=imei).first()])
    res_data = data[0]['fields']
    # print(data[0]['fields'])
    # print(data[0])
    t1 = {'2312':"dasd"}

    # return HttpResponse(res_data, content_type="application/json")
    return JsonResponse(res_data, safe=False)