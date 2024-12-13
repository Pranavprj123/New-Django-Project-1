from django.db import models
from accounts.models import Contributor
from uuid import uuid4
# Create your models here.

class MotiveType(models.TextChoices):
    SOCIAL_CAUSE = 'Social Cause','Social Cause'
    ENVIRONMENTAL = 'Environmental','Environmental'
    EDUCATIONAL = 'Educational', 'Educational'
    MEDICAL = 'Medical','Medical'
    CHARITY = 'Charity','Charity'
    OTHER = 'Other','Other'


class Motive(models.Model):
    id = models.UUIDField(primary_key=True,auto_created=True,default=uuid4())
    contributor = models.ManyToManyField(Contributor,through='InitiatorGroupContributor')
    name = models.CharField(max_length=40,unique=True)
    logo = models.ImageField(upload_to='image/motive/logo')
    motive_type = models.CharField(
        max_length=50,
        choices=MotiveType.choices,
        default=MotiveType.SOCIAL_CAUSE,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Group(models.Model):
    # id = models.UUIDField(primary_key=True,auto_created=True)
    id = models.UUIDField(primary_key=True,default=uuid4(),auto_created=True)
    created_by = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    dp = models.ImageField(upload_to="image/group/dp/")
    name = models.CharField(max_length=50,null=False,blank=False,default='')
    motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class RoleType(models.TextChoices):
    ADMIN = 'Admin','Admin'
    CREATOR = 'Creator','Creator'
    USER = 'User','User'

class InitiatorGroupContributor(models.Model):
    # id = models.UUIDField(primary_key=True,auto_created=True)
    id = models.UUIDField(primary_key=True,default=uuid4(),auto_created=True)
    contributor = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING,null=True)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50,
                            choices=RoleType.choices,
                            default=RoleType.USER)
    class Meta:
        unique_together = ['contributor','group']


class groupContributor(models.Model):
    # id = models.UUIDField(primary_key=True,auto_created=True)
    id = models.UUIDField(primary_key=True,default=uuid4(),auto_created=True)
    contributor = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50,
                            choices=RoleType.choices,
                            default=RoleType.USER)
    class Meta:
        unique_together = ['contributor','group']