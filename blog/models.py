from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='post')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title