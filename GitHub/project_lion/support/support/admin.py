from django.contrib import admin
from.models import Faq, Inquary, Answer

# Register your models here.

@admin.register(Faq)
class FqaModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)
    search_field_text = "질문 제목으로 검색이 가능합니다."
    list_filter = ('category',)


@admin.register(Inquary)
class InquaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'created_by')
    search_fields = ('title', 'email', 'phone')
    search_field_text = "제목, 이메일, 전화번호로 검색이 가능합니다."
    list_filter = ('category',)

class AnswerInline(admin.TabularInline):
    model = Inquary    
    extra = 5   
    min_num = 3
    max_num = 5
    verbose_name = "내용"   
    verbose_name_plural = "내용"





