from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField

def rewrite_slug(content):
    return content.replace(' ', '_').lower()

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    image = models.URLField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from="title", slugify_function=rewrite_slug)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f'{self.post} - {self.title}'


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.user.username


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_posts")
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
        
    def __str__(self):
        return f'{self.post.title} - {self.liker}'

