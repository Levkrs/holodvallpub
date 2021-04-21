from valdevice.models import Datatable
# def basket(request):
def menudevicelist(request):
    imei_list = []
    device_active = {}

    if request.user.is_authenticated:
        menudevice = request.user.clientlistdevice.all().only('imei',)
        for items in menudevice:
            imei_list.append(items.imei)
            # print(items.imei)
        # print(imei_list)
        # device_vall = Datatable.objects.filter(imei__in=imei_list).only('val0', 'imei','id').order_by('-id')[:5].query
        # for items in imei_list:
        #     val_dev = Datatable.objects.filter(imei=items).order_by('-id').only('val0').first()
        #     device_active[items] = val_dev.val0
        # print(device_active)

    else:
        menudevice = []
    return {
        'menudevicelist': menudevice,
    }
#     if request.user.is_authenticated:
#         basket = request.user.basket.all()
#     else:
#         basket = []
#
#     return {
#         'basket': basket,
#     }


from clientdata.models import ClientListDevice