from telnetlib import STATUS
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db import models


class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("purblished", "Published")
    )

    # DB Fields
    title = models.CharField(max_length=258)
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    purblish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    class Meta:
        ordering = ("purblish",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
