from django.contrib import admin
from core.models import Host, Participant, Contact

# Register your models here.
admin.site.register(Host)
admin.site.register(Participant)
admin.site.register(Contact)