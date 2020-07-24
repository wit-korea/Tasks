from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='list_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)
    
    def __str__(self):
        return "text:"+self.text
        # 입력받은 객체의 문자열 버전을 반환하는 함수 
        # 내장 str 클래스 의 생성자 메소드를 실행, 인자로 객체 전달 하는 것 

# 메타 옵션은 필드 단위 옵션이 아니라, 모델 단위의 옵션 
    class Meta:
        ordering = ['-created']
        # 모델의 정렬 순서 지정 : 여러개 지정 시 필드 이름을 리스트로 나열 
        # - 붙으면 내림차순, 기본은 오름차순 


    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])