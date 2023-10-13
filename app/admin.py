from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import About, Guarantee, Service, Feature, Doctor, Testimonial

@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ['title','text']
    list_display_links = ['title']
    list_editable = ['text']
    search_fields = ['title','text']

@admin.register(Guarantee)
class GuaranteeAdmin(ModelAdmin):
    list_display = ['guarantee']
    list_display_links = ['guarantee']
    search_fields = ['guarantee']

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ['title','text']
    list_display_links = ['title']
    list_editable = ['text']
    search_fields = ['title','text']

@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ['title1','title2']
    list_display_links = ['title1','title2']
    search_fields = ['title1','title2']

@admin.register(Doctor)
class DoctorAdmin(ModelAdmin):
    list_display = ['name','job','image']
    list_display_links = ['name']
    search_fields = ['name','job']

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ['name','text','proffesion','image']
    list_display_links = ['name']
    search_fields = ['name','proffesion']
    list_editable = ['text']