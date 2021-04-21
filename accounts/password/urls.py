# accounts.password.urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

app_name = 'accounts'

urlpatterns = [
    url(r'^password/change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password/change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password/reset/', auth_views.PasswordResetView.as_view(success_url = reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),

    path('password/reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('password/reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),

    path('password/reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


    # url(r'^password/reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password/reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # url(r'^password/reset/complete/$',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'),
]
