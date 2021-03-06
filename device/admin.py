from django.contrib import admin
from .models import Device, Motor, MotorData


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_meter', 'text', 'company', 'uuid', 'created_at', 'mac', 'ota_name')


class MotorAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'motor', 'fuel', 'power', 'controller', 'operation', 'capacity')


class MotorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'motor', 'day', 'yesterday')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Motor, MotorAdmin)
admin.site.register(MotorData, MotorDataAdmin)