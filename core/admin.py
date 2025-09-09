from django.contrib import admin
from .models import Project, Skill, Experience, Testimonial, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','featured','order','created_at')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
