from django.contrib import admin
from .models import Emp, Testimonial
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','phone','emp_id')
    list_editable=('phone','working')
    search_fields=('name','working')
    
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)