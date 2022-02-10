from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime


# Create your models here.


class Parent(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        NA = 'NA', _('NA')

    name = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=30, blank = True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.NA)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Course(models.Model):
    name = models.CharField(max_length=200, blank = False)
    description = models.TextField(null = True, blank = True)
    # videoLecture  = models.ManyToManyField(VideoLecture, blank=True, null = True)
    # liveLecture = models.OneToOneField(LiveLecture, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.name


class Child(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        NA = 'NA', _('NA')

    parent = models.ForeignKey(Parent,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dob = models.DateField(blank=False, null= True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.NA)
    course = models.ManyToManyField(Course, blank=True)
    enrolled = models.BooleanField(blank=True, null=True)
    monthly_fees = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Fees(models.Model):

    class Month(models.TextChoices):
        one = 'one_time', _('One Time')
        jan = 'january', _('January')
        feb = 'february', _('February')
        mar = 'march', _('March')
        apr = 'april', _('April')
        may = 'may', _('May')
        jun = 'june', _('June')
        jul = 'july', _('July')
        aug = 'august', _('August')
        sep = 'september', _('September')
        oct = 'october', _('October')
        nov = 'november', _('Novemeber')
        dec = 'december', _('December')

    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    month = models.CharField(max_length=15, choices=Month.choices, default=Month.one)
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=False, null= True, default=datetime.date.today)
    payment_method = models.CharField(max_length=20, null=True, blank=True)
    Notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.child.name + " " + self.month

