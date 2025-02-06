from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  query_set = ('first_name', 'last_name', 'email', 'role', 'is_active')
  search_fields = ('email', 'role', 'is_active')

admin.site.register(User, UserAdmin)