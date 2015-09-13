from django.contrib import admin
from buku2.models import Category, Book
from buku2.models import UserProfile

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(UserProfile)


# Register your models here.
