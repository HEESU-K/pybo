from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model): # 테이블 모델명 Question / 속성 3개 subject, content, create_date
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question')
    subject = models.CharField(max_length = 200) # 글자수 길이 제한된 텍스틑 CharField 사용
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') #추천인 추가
    oppose = models.ManyToManyField(User, related_name='oppose_question')


    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_data = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    oppose = models.ManyToManyField(User, related_name='oppose_answer')
