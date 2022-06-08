from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    CATEGORY_ONE = '1'
    CATEGORY_CHOICES=[
        (CATEGORY_ONE,'일반'),
        ('2','계정'),
        ('3','기타')
]
    title = models.TextField(verbose_name='질문 제목', max_length=80)
    content = models.TextField(verbose_name="질문 내용")
    category = models.CharField(verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICES)
    reply = models.TextField(verbose_name='답변')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='faq_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='faq_updated_by')

    

class Inquary(models.Model):
    CATEGORY_CHOICES=[
        ('1','일반'),
        ('2','계정'),
        ('3','기타')
]
    title = models.CharField(verbose_name="질문 제목", max_length=80)
    category = models.CharField(verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICES)
    email = models.EmailField(verbose_name="이메일", blank=True)
    phone = models.CharField(verbose_name="문자메시지", max_length=11, blank=True)
    is_email = models.BooleanField(verbose_name='이메일 수신 여부', default=True)
    is_phone = models.BooleanField(verbose_name='문자메시지 수신 여부', default=True)
    content = models.TextField(verbose_name="문의 내용")
    image = models.ImageField(verbose_name="이미지", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="생성 일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="최종 수정 일시", auto_now_add=True)

    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquary_updated_by')
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='inquary_created_by')

class Answer(models.Model):
    content = models.TextField(verbose_name="답변 내용")
    created_at = models.DateTimeField(verbose_name="생성 일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="최종 수정 일시", auto_now_add=True)

    inquary = models.ForeignKey(to="Inquary", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_updated_by')
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_created_by')
