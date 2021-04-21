from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('client/', include('clientdata.urls', namespace='clientdata')),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('accounts.password.urls')),

]
