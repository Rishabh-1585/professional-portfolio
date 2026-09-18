from django.contrib import admin
from .models import Skill, About, Experience, Certification, Resume

admin.site.register(Skill)
admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Resume)