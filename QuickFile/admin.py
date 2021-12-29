from django.contrib import admin
from . models import CBC, ClientInfo, Lipid_Profile, KFT, LFT

# Register your models here.
admin.site.register(CBC)
admin.site.register(LFT)
admin.site.register(KFT)
admin.site.register(Lipid_Profile)
