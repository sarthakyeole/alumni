from django.db import models
import datetime, os
from time import strftime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


def upload_blog_photo(instance, filename):
    name, extension = os.path.splitext(filename)
    return "Blog/" + str(instance.blog_id) + extension


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    by = models.TextField(max_length=500)
    picture = models.ImageField(null=True, blank=True, upload_to=upload_blog_photo)
    description = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title_stripped

    @property
    def title_stripped(self):
        from django.utils.html import strip_tags
        return strip_tags(self.title)
