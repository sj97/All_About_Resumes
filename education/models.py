from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed= models.BooleanField(default=False)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    website = models.URLField(blank=True)


class Education(models.Model):
    CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # PERSONAL DETAILS
    name = models.CharField(max_length=100, default='')
    homeadd = models.CharField(max_length=200, default='N/A')
    dob = models.DateField(default='2000-12-20')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    gender = models.CharField(max_length=3, choices=CATEGORIES)

    # yoc1 is for Xth
    yoc1 = models.IntegerField(default='2000')
    board1= models.CharField(max_length=200, default='')
    percentage1 = models.IntegerField(default='0')
    # email = models.EmailField()

    # yoc2 is for XIIth
    yoc2 = models.IntegerField(default='2000')
    board2 = models.CharField(max_length=200, default='')
    percentage2 = models.IntegerField(default='0')

    #GRADUATION DETAILS
    yoc3 = models.IntegerField(blank=True, default='2000')  # yoc3 is for graduation
    percentage3 = models.IntegerField(default='0', blank=True)
    college = models.CharField(max_length=100, default='N/A', blank=True)
    course = models.CharField(max_length=20, default='N/A', blank=True)

    #INTERNSHIP DETAILS
    company_i = models.CharField(max_length=200, default='N/A', blank=True)
    duration = models.IntegerField(default= 0, blank=True)
    profile_i=models.CharField(max_length=20, default='N/A', blank=True)

    # INTERNSHIP DETAILS 2
    company_i2 = models.CharField(max_length=200, default='N/A', blank=True)
    duration2 = models.IntegerField(default=0, blank=True)
    profile_i2 = models.CharField(max_length=20, default='N/A', blank=True)

    #MAIN SEARCH MODULE
    work = models.CharField(max_length=100, default='',)

    #PROJECT
    title_p=models.CharField(max_length=30,default='N/A', blank= True)
    description_p= models.CharField(max_length=1000, default='N/A', blank=True)

    #SKILLS
    skills= models.CharField(max_length=1000, default='')

    #LINKS
    git_hub = models.URLField(default='',  blank=True)
    linked_in = models.URLField(default='', blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



