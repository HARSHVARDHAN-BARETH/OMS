from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null = True, blank = True)


class Department(models.Model):
    name = models.CharField(max_length=180, null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="-----", max_length=200, null=True)
    title = models.CharField(default="---------", max_length=200, null=True)
    desc_text = "--------------"
    desc = models.CharField(default=desc_text, max_length=200, null=True)
    profileImg = models.ImageField(default="media/default.jpg",upload_to='media', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username}s Profile'


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hireDate = models.DateField()
    def __str__(self):
        return "%s %s %s"%(self.first_name, self.last_name, self.phone)

    
    
