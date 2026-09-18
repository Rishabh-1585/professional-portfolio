from django.db import models


class Skill(models.Model):

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class About(models.Model):

    introduction = models.TextField()

    professional_summary = models.TextField()

    career_objective = models.TextField()

    what_i_do = models.TextField()

    my_approach = models.TextField()

    def __str__(self):
        return "About Me"

class Experience(models.Model):

    company = models.CharField(max_length=200)

    role = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField(blank=True, null=True)

    description = models.TextField()

    responsibilities = models.TextField(blank=True)

    technologies = models.CharField(max_length=300, blank=True)

    achievements = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} - {self.company}"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    issued_by = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(blank=True, null=True)
    certificate = models.FileField(upload_to="certificates/")

    def __str__(self):
        return self.name

class Resume(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="resume/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title