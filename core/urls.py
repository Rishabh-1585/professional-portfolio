from django.urls import path
from .views import home, about, skills, experience, education, certifications, resume
from contact.views import contact
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("skills/", skills, name="skills"),
    path("experience/", experience, name="experience"),
    path("education/", education, name="education"),
    path("certifications/", certifications, name="certifications"),
    path("resume/", resume, name="resume"), 
    path("contact/", contact, name="contact"),
]

