from django.contrib import admin
from .models import Subject, Course, Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """ This creates a custom admin class for the Subject model.
        It inherits from admin.ModelAdmin, which provides a set of default behaviors for the admin interface.
    """
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    


class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]