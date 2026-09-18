from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "about",
            "skills",
            "projects",
            "experience",
            "education",
            "certifications",
            "resume",
            "blog",
            "contact",
        ]

    def location(self, item):
        return reverse(item)