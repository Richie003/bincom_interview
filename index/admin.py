from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AgentName)
admin.site.register(Announced_lga_results)
admin.site.register(Announced_pu_results)
admin.site.register(Announced_state_results)
admin.site.register(Announced_ward_results)
admin.site.register(LGA)
admin.site.register(Party)
admin.site.register(Polling_unit)
admin.site.register(States)
admin.site.register(Ward)


