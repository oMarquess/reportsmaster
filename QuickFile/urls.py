from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('cbc_root/cbc', views.cbc, name = 'cbc'),
    path('cbc_root/cbc-profile/<str:pk>', views.cbc_profile, name = 'cbc-profile'),
    path('cbc_root/delete-cbc-profile/<str:pk>', views.delete_cbc, name = 'delete_cbc'),
    path('cbc_root/cbc-report/<str:pk>', views.generate_cbc_report, name = 'cbc_report'),

    path('kft_root/kft', views.kft, name = 'kft'),
    path('kft_root/kft-profile/<str:pk>', views.kft_profile, name = 'kft-profile'),
    path('kft_root/delete-kft-profile/<str:pk>', views.delete_kft, name = 'delete_kft'),
    path('kft_root/kft-report/<str:pk>', views.generate_kft_report, name = 'kft_report'),

    path('lft_root/lft', views.lft, name = 'lft'),
    path('lft_root/lft-profile/<str:pk>', views.lft_profile, name = 'lft-profile'),
    path('lft_root/delete-lft-profile/<str:pk>', views.delete_lft, name = 'delete_lft'),
    path('lft_root/lft-report/<str:pk>', views.generate_lft_report, name = 'lft_report'),


    path('lpd_root/lpd', views.lpd, name = 'lpd'),
    path('lpd_root/lpd-profile/<str:pk>', views.lpd_profile, name = 'lpd-profile'),
    path('lpd_root/delete-lpd-profile/<str:pk>', views.delete_lpd, name = 'delete_lpd'),
    path('lpd_root/lpd-report/<str:pk>', views.generate_lpd_report, name = 'lpd_report')






] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)