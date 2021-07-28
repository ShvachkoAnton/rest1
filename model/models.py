from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your models here.
class Group(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()

    def __str__(self):
        return self.title



class Post(models.Model):
    author=models.ForeignKey('auth.User',related_name='snippets', on_delete=models.CASCADE)
    text=models.TextField()
    snippets=models.TextField()
    highlight=models.TextField()
    group=models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group', blank=True,null=True)
    pub_date=models.DateTimeField('дата публикации', auto_now_add=True)
    image=models.ImageField(upload_to='posts/',null=True,blank=True)
    def __str__(self):
        return self.text

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        unique_together = ("user", "author")