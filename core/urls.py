from django.contrib import admin
from django.urls import path
from api.views import LoginView,SaveFile,AddedTask,CreateUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',LoginView.as_view()),
    path('home/<int:id>',SaveFile.as_view()),
    path('add_task/',AddedTask.as_view()),
    path('add_user/',CreateUser.as_view()),
]
