"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# По умолчанию в проект Django подключена система администрирования
from django.contrib import admin
# Функция include позволит использовать path() из других файлов.
# Импортируем!
from django.urls import include, path


urlpatterns = [
    # Дорогой Джанго, если на сервер пришёл любой запрос (''),
    # перейди в файл urls приложения posts
    # namespace позволяет избегать дублирования path() с одинаковыми name.
    # и проверь там все path() на совпадение с запрошенным URL
    # namespace указывают имя, совпадающее с названием приложения.
    path('', include('posts.urls', namespace='posts')),
    # Если в приложении posts не найдётся совпадений -
    # Django продолжит искать совпадения здесь, в головном файле urls.py.
    # Встроенная админка Django подключена «из коробки» по адресу admin/
    path('admin/', admin.site.urls),
    path('group/<slug:slug>/', include('posts.urls')),
]
