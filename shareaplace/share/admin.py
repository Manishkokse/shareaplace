from django.contrib import admin
from .models import SignUp
# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    model=SignUp
    list_display = ['firstname','lastname','email']
    ordering=('firstname',)




admin.site.register(SignUp,SignUpAdmin)
