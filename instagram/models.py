from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True,upload_to="instagram/post/%y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank= True)
    #M2M에서 blank를 True로 설정을 하는 것은 의미가 있다.
    #balnk를 True 로 하지 않으면 Post를 만들때 꼭 Tag를 만들어야 하기 때문에
    #django의 유효성 검사에서 오류가 날수 있다.
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
