from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""注册新用户"""
	if request.method != 'POST':
		# 显示空的注册图表
		form = UserCreationForm()
	else:
		# 处理填写好的表单
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			login(request, new_user)
			return redirect('learning_logs:index')

	# 展示空表或者指出表单无效
	context = {'form': form}
	return render(request, 'registration/register.html', context)
