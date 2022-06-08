from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):   #StackedInline
    model = Comment     #댓글 갯수 지정
    extra = 5   
    min_num = 3
    max_num = 5
    verbose_name = "댓글"
    verbose_name_plural = "댓글"


# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content','image','writer','created_at','view_count')
    #list_editable = ('content')
    list_filter = ('created_at',)
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at', )
    inlines = [CommentInline]

    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규졍 위반으로 인한 게시글 삭제 처리'
            item.save() 
        

#admin.site.register(Comment)