from rest_framework.views import APIView
from rest_framework.response import Response#FileResponse
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from .serilezer import LessonSerializer
from .models import Lesson,Status,SendTask,Tasks,Rating,Books
from django.http import FileResponse
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user=request.user
        name=user.first_name
        try:
            token=Token.objects.get(user=user)
            data=[{'token':token.key,'type':name}]
        except:
            token=Token.objects.create(user=user)
            data=[{'token':token.key,'type':name}]
        try:
            tasks=Tasks.objects.all()
            for task in tasks:
                try:
                    hwk = SendTask.objects.get(task=task, user=user)
                    status = 'Topshirdi'
                    rate = 0.0
                    try:
                        rate = Rating.objects.get(user=user,hwk=hwk)
                        status = 'Baholandi'
                        rate = rate.rate
                    except:
                        status = 'Topshirdi'
                        rate = 0.0
                except:
                    status = 'Berildi'
                    rate = 0.0
                url=f'https://eduhemisuz.pythonanywhere.com/home/{task.id}'
                data.append({
                    'id':task.id,
                    'name':task.name,
                    'file_name':task.file.name,
                    'file':url,
                    'description':task.description,
                    'status':status,
                    'rating':rate
                })
            return Response(data)
        except:
            return Response({"error":'Not Found'})



class SaveFile(APIView):
    def get(self,request,id):
         document=Tasks.objects.get(id=id)
         file = open(document.file.path, 'rb')
        # Return the file as a `FileResponse`
         response = FileResponse(file)
         print(response)
         return response
class SaveWork(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self,request,id):
        document=SendTask.objects.get(id=id)
        file = open(document.file.path, 'rb')
            # Return the file as a `FileResponse`
        response = FileResponse(file)
        return response
class SaveBook(APIView):
    def get(self,request,id):
        document=Books.objects.get(id=id)
        file = open(document.file.path, 'rb')
            # Return the file as a `FileResponse`
        response = FileResponse(file)
        return response

class AddedTask(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user=request.user
        upload = request.FILES['file']
        data = request.data
        task=Tasks.objects.create(
            name=data['name'],
            file=upload,
            description=data['description'],
            rating=0.0,
            status='Berildi'
        )
        task.save()
        return Response({'response':'OK'})

class CreateUser(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        user = request.user
        if user.first_name == 'teacher':
            try:
                data = request.data
                user = User.objects.create(
                    username = data['username'],
                    first_name = 'student',
                    password = make_password(data['password'])
                )
                user.save()
                return Response({'success': 'Done'})
            except:
                return Response({'success': 'Error'})
        else:
            return Response({'success': 'Ruxsat yo\'q'})
class SendWork(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self,request,id):
        user=request.user
        first_name=user.first_name
        if first_name=='teacher':
            try:
                task=Tasks.objects.get(id=id)
                hwks=SendTask.objects.filter(task=task)
                result=[]
                for hwk in hwks:
                    try:
                        rate = Rating.objects.get(hwk=hwk)
                        rating=rate.rate
                        result.append({
                            'id':hwk.id,
                            'file_name':hwk.file.name,
                            'file':f'https://eduhemisuz.pythonanywhere.com/save/{hwk.id}',
                            'user':hwk.user.username,
                            'rating':rating
                        })
                    except:
                        rate=False
                        result.append({
                            'id':hwk.id,
                            'file_name':hwk.file.name,
                            'file':f'https://eduhemisuz.pythonanywhere.com/save/{hwk.id}',
                            'user':hwk.user.username,
                            'rating':rate
                        })
                return Response(result)
            except:
                return Response({'status':'error'})
    def post(self, request):
        userb = request.user
        first_name = userb.first_name
        if first_name == 'student':
            data=request.data
            try:
                upload = request.FILES['file']
                task = Tasks.objects.get(id=data['id'])
                user=User.objects.get(username=data['username'])
                hwk=SendTask.objects.create(
                    file = upload,
                    task = task,
                    user = user
                )
                hwk.save()
                return Response({'status':'Qo\'shildi'})
            except:
                return Response({'status':'Bad Request'})
    def put(self,request):
        data=request.data
        try:
            task=SendTask.objects.get(id=data['task_id'])
            rate=Rating.objects.create(
                rate=data['rate'],
                user=task.user,
                hwk = task
            )
            task.save()
            return Response({'status':'Done'})
        except:
            return Response({'status':'bad request'})

class BooksView(APIView):
    def get(self,request):
        try:
            books=Books.objects.all()
            data=[{'status':'OK'}]
            for book in books:
                data.append({
                    'id':book.id,
                    'name':book.name,
                    'file_name':book.file.name,
                    'file':f'https://eduhemisuz.pythonanywhere.com/save_book/{book.id}'
                })
            return Response(data)
        except:
            return ({'status':'error'})
    def post(self,request):
        try:
           upload = request.FILES['file']
           data = request.data
           book=Books.objects.create(
               name = data['name'],
               file = upload
           )
           book.save()
           return Response({'success': True})
        except:
            return Response({'success': False})




