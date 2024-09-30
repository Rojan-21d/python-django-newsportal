from django.contrib import admin
from newspaper.models import (
    Post,
    Category,
    Tag,
    Contact,
    UserProfile,
    Comment,
    Newsletter,
)
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)


# uta admin site ma dekhaune kaam esle garxa
admin.site.register([Category, Tag, Contact, UserProfile, Comment, Newsletter])

# summernotes ko
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)



admin.site.register(Post, PostAdmin)
