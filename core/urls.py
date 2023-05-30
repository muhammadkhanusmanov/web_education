from django.contrib import admin
from django.urls import path
from api.views import LoginView,SaveFile,AddedTask,CreateUser,SendWork,SaveWork,SaveBook,BooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',LoginView.as_view()),
    path('home/<int:id>',SaveFile.as_view()),
    path('add_task/',AddedTask.as_view()),
    path('add_user/',CreateUser.as_view()),
    path('send_work/',SendWork.as_view()),
    path('save/<int:id>',SaveWork.as_view()),
    path('getwork/<int:id>',SendWork.as_view()),
    path('save_book/<int:id>',SaveBook.as_view()),
    path('books/',BooksView.as_view()),
]
