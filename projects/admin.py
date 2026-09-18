from django.contrib import admin
from .models import Project , ProjectFile, ProjectImage


admin.site.register(Project)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
