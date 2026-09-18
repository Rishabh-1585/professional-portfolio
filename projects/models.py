from django.db import models


class Project(models.Model):

    # =========================
    # BASIC PROJECT INFORMATION
    # =========================

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    short_description = models.TextField()

    description = models.TextField()


    # =========================
    # PROJECT CASE STUDY
    # =========================

    business_problem = models.TextField(blank=True)

    objective = models.TextField(blank=True)

    dataset = models.TextField(blank=True)

    methodology = models.TextField(blank=True)

    analysis = models.TextField(blank=True)

    insights = models.TextField(blank=True)

    recommendations = models.TextField(blank=True)

    challenges = models.TextField(blank=True)

    results = models.TextField(blank=True)


    # =========================
    # TECHNOLOGIES & LINKS
    # =========================

    technologies = models.CharField(max_length=300)

    github_link = models.URLField(blank=True)

    live_link = models.URLField(blank=True)


    # =========================
    # PROJECT SETTINGS
    # =========================

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


# ==================================================
# PROJECT FILES
# ==================================================

class ProjectFile(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="files"
    )

    name = models.CharField(max_length=200)

    file = models.FileField(
        upload_to="project_files/"
    )

    description = models.CharField(
        max_length=300,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="project_images/"
    )

    description = models.CharField(
        max_length=300,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title