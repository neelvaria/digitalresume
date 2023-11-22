from django.contrib import admin
from.models import *
# Register your models here.

@admin.register(UserProfile)
class userprofileadmin(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(ContactProfile)
class Contactadmin(admin.ModelAdmin):
    list_display = ('id','timestamp','name')

@admin.register(Testimonial)
class testi(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(media)
class mediacon(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Portfolio)
class port(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class blogg(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class cert(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class skil(admin.ModelAdmin):
    list_display = ('id','name','score')