from django.contrib import admin
from .models import Action,Organism,Campaign,CustomInfo,Payment

# Register your models here.
admin.site.register(Action)
admin.site.register(Campaign)
admin.site.register(CustomInfo)
admin.site.register(Organism)
admin.site.register(Payment)