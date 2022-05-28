from django.urls import path
from . import views


# В urls.py подключаемого приложения должна быть объявлена переменная
# app_name, в которой тоже указывается namespace для путей приложения:
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Отдельная страница с информацией о группе
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
