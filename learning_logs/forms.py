#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : fiuxiu
# @Time    : 2020年11月29日 17:29
# @Software: PyCharm
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic  # 根据模型Topic创建表单 其中只包含字段text
		fields = ['text']
		labels = {'text': ''}  # 让Django不要为字段text生成标签


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ' '}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}   # 文本区域宽度80


