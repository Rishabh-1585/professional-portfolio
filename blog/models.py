from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True
    )
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title