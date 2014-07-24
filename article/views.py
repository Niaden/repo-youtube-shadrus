# coding: utf8
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments

# Create your views here.

def basic_one(request):
	view = 'basic_one'
	html = "<html><body>THis is %s view </body></html>" % view
	return HttpResponse(html)

def template_two(request):
	view = "template_two"
	t = get_template('myview.html')
	html = t.render(Context({'name': view}))
	return HttpResponse(html)

def template_three_simple(request):
	view = "template_three"
	return render_to_response('myview.html', {'name': view})

def articles(request):
	return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id=1):
	#objects.get - юзать только, когда 1 объект(в нашем случае, запись) возвращаешь(если признаку в get будут удовлетворять более, чем 1 объект, будет ошибка). objects.filter - то же самое, только возвращается несколько объектов по признаку возвращаешь.
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})