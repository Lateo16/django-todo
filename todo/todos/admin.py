from django.contrib import admin
from .models import Todo
from .form import TodoForm


class LeaveAdmin(admin.ModelAdmin):
    form = TodoForm


admin.site.register(Todo, LeaveAdmin)