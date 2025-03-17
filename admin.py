from django.contrib import admin
from .models import Todo
from django_summernote.admin import SummernoteModelAdmin  # summernote 사용을 위한 import

# Todo 모델에 대한 admin 설정
class TodoAdmin(SummernoteModelAdmin):  # SummernoteModelAdmin을 상속받아 summernote를 사용할 수 있도록 함
    list_display = ('title', 'start_date', 'end_date', 'is_completed')  # 목록에서 보여줄 필드들
    search_fields = ['title', 'description']  # 검색할 수 있는 필드
    list_filter = ['is_completed']  # 필터링 가능한 필드

    # fieldsets를 이용하여 필드 배치
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'start_date', 'end_date', 'is_completed', 'completed_image')  # completed_image 추가
        }),
    )

    # Summernote를 description 필드에 적용
    summernote_fields = ('description',)  # description에만 Summernote 적용

# admin에 TodoAdmin 등록
admin.site.register(Todo, TodoAdmin)

