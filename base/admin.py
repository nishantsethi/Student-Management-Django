from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Parent)
admin.site.register(Course)
admin.site.register(Child)
admin.site.register(Fees)

admin.site.site_header = "Kids Planet School"
admin.site.site_title = "Kids Planet Portal"
admin.site.index_title = "Welcome to KPS Portal"