from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FollowRelation(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()
    follower = models.OneToOneField(
        User, related_name='follower', on_delete=models.CASCADE)  # 나를 팔로우 하는 사람
    followee = models.ManyToManyField(User, related_name='followee')  # 내가 팔로우
