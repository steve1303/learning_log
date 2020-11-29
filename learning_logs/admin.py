from django.contrib import admin

# Register your models here.
from .models import Topic, Entry  # 在admin.py 所在的目录下查找models.py

admin.site.register(Topic)  # 让Django通过管理网站管理模型
admin.site.register(Entry)

