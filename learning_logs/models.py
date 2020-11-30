from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):  # 继承自Model
	"""用户学习的主题"""
	text = models.CharField(max_length=200)  # 属性text是由字符组成的数据 即文本（少量数据）
	date_added = models.DateTimeField(auto_now_add=True)  # 记录日期和时间的数据
	# 每当用户创建新主题时，Django会将这个属性自动设置为当前日期和时间

	owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 建立外键关联

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text


class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键实例 级联删除
	text = models.TextField()  # TextField实例  字段长度不受限制
	date_added = models.DateTimeField(auto_now_add=True)  # 按照创建顺序呈现条目，并在每个条目之间放置时间戳

	class Meta:  # 嵌套类 存储管理模型的额外信息
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		return f"{self.text[:30]}..."
