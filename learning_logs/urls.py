"""定义learning_logs的URL模式"""

from django.urls import path  # 导入path 将URL映射到视图

from . import views  # 导入模块views 句点. 让python从当前urls.py 模块所在的文件夹导入views.py

app_name = 'learning_logs'  # 命名空间
urlpatterns = [
	# 主页
	path('', views.index, name='index'),
	# 显示所有主题
	path('topics/', views.topics, name='topics'),
	# 特定主题的详细页面
	path('topics/<int:topic_id>/', views.topic, name='topic'),
]

# urlpatterns 是个列表，包含所有可在应用程序learning_logs中请求的页面
# URL模式就是对path()函数的调用 这个函数接受三个实参
"""
第一个是一个字符串，帮助Django正确的路由(route)请求。
收到请求的URL后，Django力图将请求路由给一个视图。
为此，它将搜索所有的URL模式，找到与当前请求匹配的那个。
Django忽略项目的基础URL(http://localhost:8000/)，
因此(‘‘)空字符串和基础的URL匹配，其他URL都与这个模式不匹配。
如果请求的URL与任何既有的URL都不匹配,Django将返回一个错误页面。
"""
"""
第二个实参指定了要调用views.py中的哪个函数。
请求的URL与前述正则表达式匹配时，Django将调用views.py中的函数index
"""
"""
第三个实参将这个URL模式的名称指定为index，让我们能在代码的其他地方引用它。
每当需要提供到这个主页链接时，都使用这个名称，而不是编写URL。
"""