from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return self.user



#from django.contrib.auth import get_user_model
#user = get_user_model()
#user = User.objects.first() 현재 활성화된 User모델
#user.profile