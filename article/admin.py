# coding: utf8
from django.contrib import admin
from .models import Article, Comments

# Register your models here.
# добавляем комментарии в админку, связанные с объектом статьи
class ArticleInLine(admin.StackedInline):
	model = Comments
	# переменная extra для кол-ва отображения комментариев к 1й статье
	extra = 2

#управление отображением Article
class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title','article_text','article_date']
	inlines = [ArticleInLine]
	#добавляем фильтрацию статей по дате
	list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)
# регистрируем класс, которым можно управлять в админке, и класс, который управляет отображением класса Article