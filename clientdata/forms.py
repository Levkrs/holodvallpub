from clientdata.models import ClientListDevice, NameValueClientDevice
from django.forms import forms, ModelForm, HiddenInput
from valdevice.models import Datatable
from django import forms

class ClientListDeviceForm(ModelForm):
    class Meta:
        model = NameValueClientDevice
        fields = '__all__'
        # exclude = ('imei_device',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'

class ClientDeviceValShowForm(ModelForm):
    class Meta:
        model = Datatable
        fields = '__all__'


class ClientAddDeviceForm(ModelForm):
    class Meta:
        model = ClientListDevice
        fields = '__all__'
        exclude = ('date_add', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'user':
                field.widget = HiddenInput()
            field.widget.attrs['class'] = f'form-control {field_name}'

class ClientUpdateDeviceForm(ModelForm):
    class Meta:
        model = NameValueClientDevice
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'imei_device':
                field.widget = HiddenInput()
            field.widget.attrs['class'] = f'form-control {field_name}'

class DataInputForm(forms.Form):
    # date_val_start = forms.DateField(label="Начальная дата", input_formats=['%d/%m/%Y'])
    date_val_start = forms.DateField(label="Начальная дата", input_formats=['%Y-%m-%d'])

    # date_val_end = forms.DateField(label="Конечная дата", input_formats=['%d/%m/%Y'])
    date_val_end = forms.DateField(label="Конечная дата", input_formats=['%Y-%m-%d'])


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'date_val_start':
                field.widget.attrs['class '] = f'datepicker'
                field.widget.attrs['data-date-format'] = f'yyyy-mm-dd'

                field.widget.attrs['id'] = f'datepicker'
            if field_name == 'date_val_end':
                field.widget.attrs['class '] = f'datepicker'
                field.widget.attrs['data-date-format'] = f'yyyy-mm-dd'
                field.widget.attrs['id'] = f'datepicker1'