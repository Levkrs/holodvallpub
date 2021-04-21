from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from django.contrib.auth import views as auth_views

import mainapp.views as mainapp
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('register/', authapp.userRegister, name='register'),
    path('logout/', authapp.logout, name='logout'),
    path('profile/', authapp.profile, name='profile'),
    path('verify/<str:email>/<str:activation_key>/', authapp.verify, name='verify'),

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="authapp/reset_password.html",
    #                                                              success_url = reverse_lazy('authapp:password_reset_sent'),
    #                                                              ),
    #      name='reset_password'),
    #
    #
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="authapp/password_reset_sent.html"),
    #      name='password_reset_sent'),
    #
    #
    # path('auth/reset/<uidb64>/<token>',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="authapp/password_reset_form.html"),
    #      name='password_reset_confirm'),
    #
    #
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="authapp/password_reset_done.html"),
    #      name='password_reset_complete'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name="authapp/reset_password.html", success_url = reverse_lazy('authapp:password_reset_done')), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
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
