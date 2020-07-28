from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #Refer the Lecture 
 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #additional Class
    #using portfolio if it is a portfolio website and we use Blank so that the user can even leave it blank without getting an error
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    #now if the user uploads Profile pic then it is stored in the profile_pics folder under media folder
    def __str__(self):
        return self.user.username