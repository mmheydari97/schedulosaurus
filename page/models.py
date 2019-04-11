from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from django_jalali.db import models as jmodels

# Create your models here.
import datetime
from django.utils import timezone

phone_regex = RegexValidator(regex=r'^\+?98?\d{9,15}$', message="Phone number up to 15 digits is allowed.")


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    def __str__(self):
        return self.user_id.username


class Packet(models.Model):
    objects = jmodels.jManager()
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    sDate = jmodels.jDateTimeField('Date Created', auto_now_add=True)

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.sDate.year, self.sDate.month,self.sDate.day)


class Task(models.Model):
    title = models.CharField(max_length=100)
    sTime = models.TimeField('Time Started', auto_now_add=True)
    eTime = models.TimeField('Time Ended', blank=True, null=True)
    box_id = models.ForeignKey(Packet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_date(self):
        pass

    def get_duration(self):
        t2 = self.eTime.hour*60 + self.eTime.minute
        t1 = self.sTime.hour*60 + self.sTime.minute
        res = ''
        hours = (t2-t1)//60
        minutes = (t2-t1) % 60
        if hours != 0:
            res += '{} ساعت'.format(hours)

        if hours != 0 and minutes != 0:
            res += ' و '
        if minutes != 0:
            res += '{} دقیقه'.format(minutes)
        if res == '':
            res = '۰'
        return res

