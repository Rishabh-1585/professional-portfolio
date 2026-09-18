from django.http import HttpResponse
from django.shortcuts import render
from .models import Skill, About, Experience, Certification, Resume

def home(request):

    skills = Skill.objects.all()[:4]

    return render(request, "home.html", {
        "skills": skills
    })

def about(request):
    about = About.objects.first()

    return render(request, "about.html", {
        "about": about
    })

def skills(request):
    skills = Skill.objects.all()

    return render(request, "skills.html", {
        "skills": skills
    })

def projects(request):
    return render(request, "projects.html")

def experience(request):
    experiences = Experience.objects.all().order_by("-start_date")

    return render(request, "experience.html", {
        "experiences": experiences
    })

def education(request):
    return render(request, "education.html")

def certifications(request):
    certifications = Certification.objects.all().order_by("-issue_date")
    return render(
        request,
        "certifications.html",
        {"certifications": certifications}
    )

def resume(request):
    resume = Resume.objects.last()
    return render(request, "resume.html", {"resume": resume})


def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def robots_txt(request):
    return HttpResponse(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Sitemap: /sitemap.xml",
        content_type="text/plain"
    )