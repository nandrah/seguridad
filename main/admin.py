from main.models import Hacker, Comment, Enterprise, Service, Job
from django.contrib import admin


class ServiceInLine(admin.StackedInline):
    model = Service
    extra = 3


class EnterpriseAdmin(admin.ModelAdmin):
    inlines = [ServiceInLine]


admin.site.register(Hacker)
admin.site.register(Comment)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Service)
admin.site.register(Job)
