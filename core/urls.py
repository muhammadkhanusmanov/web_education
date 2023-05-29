from django.contrib import admin
from django.urls import path
from api.views import LoginView,SaveFile,AddedTask,CreateUser,SendWork,SaveWork

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',LoginView.as_view()),
    path('home/<int:id>',SaveFile.as_view()),
    path('add_task/',AddedTask.as_view()),
    path('add_user/',CreateUser.as_view()),
    path('rated/',SendWork.as_view()),
    path('send_work/',SendWork.as_view()),
    path('save/<int:id>',SaveWork.as_view()),
    path('getwork/<int:id>',SendWork.as_view),
]
