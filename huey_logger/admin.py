from django.contrib import admin
from .models import LastCronRun, CronError


@admin.register(LastCronRun)
class LastCronRunAdmin(admin.ModelAdmin):
    list_display = ('name', 'started_at', 'ended_at')

    def get_readonly_fields(self, request, obj=None):
            return [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_save_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(LastCronRunAdmin, self).changeform_view(
            request, object_id,
            extra_context=extra_context
        )


@admin.register(CronError)
class CronErrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'error')

    def get_readonly_fields(self, request, obj=None):
            return [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def has_save_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(CronErrorAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )
