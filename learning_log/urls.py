from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # 包含应用程序users定义的URL
    path('', include('learning_logs.urls')),
]
# 包括learning_logs.urls
# 包括users.urls
