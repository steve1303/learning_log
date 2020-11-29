from django.shortcuts import render

from .models import Topic


# 向对象request传递两个实参，request和一个可以用于创建页面的模板
# html本质是一个字符串，只不过浏览器认识它，可以将其解析成页面。
# 模板定义页面的外观，每当页面被请求时，Django将填入相关的数据。
# 模板能够让你访问视图提供的任何数据。
def index(request):  # 视图函数
	"""学习笔记的主页"""
	return render(request, 'learning_logs/index.html')


def topics(request):
	"""显示所有的主题"""
	topics = Topic.objects.order_by('date_added')  # 查询数据库 请求提供Topic对象
	context = {'topics': topics}   # 定义上下文字典
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	"""显示单个主题及其所有的条目"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)