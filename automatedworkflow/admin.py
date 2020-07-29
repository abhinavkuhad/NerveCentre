from django.contrib import admin
from .models import NewsCentre
from .models import Journalist
from .models import ResourceCentre

# Register your models here.

admin.site.register(NewsCentre)
admin.site.register(Journalist)
admin.site.register(ResourceCentre)