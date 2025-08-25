from django.db import models
from django.contrib.auth.models import User

""" 
create table posts(id integer promary key autoincrement not null, title varchar(256) not null, content varchar(556));
"""
"""
select * from posts ==>Post.objects.all()
"""
"""select * from posts where title ILIKE '%p%' ==> Post.objects.filter(title__icontains='probably') limit 10
"""
"""select 1 from posts where id = 123 ==> Post.objects.get(id=123)
"""
"""INSERT INTO posts(title, content) VALUES('title', 'content') ==>Post.objects.create(title='title', content='content')
"""

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=256)
    img = models.ImageField(upload_to='media/', null=True)
    content = models.CharField(max_length=256, null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User), on_delete=models.CASCADE, null=True

    def __str__(self):
        return f"self.title - {self.content}"

# Create your models here.
