from rest_framework.views import APIView
from rest_framework.response import Response#FileResponse
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from .serilezer import LessonSerializer
from .models import Lesson,Status
from django.http import FileResponse
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



# def doc(request,id, format=None):
#     document=Lesson.objects.get(id=id)
#     file = open(document.file.path, 'rb')
#         # Return the file as a `FileResponse`
#     response = FileResponse(file)
#     return response

class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user=request.user
        try:
            token=Token.objects.get(user=user)
            data=[{'token':token.key}]
        except:
            token=Token.objects.create(user=user)
            data=[{'token':token.key}]
        try:
            tasks=Lesson.objects.filter(users=user)
            for task in tasks:
                url=f'http://eduhemisuz.pythonanywhere.com/home/{task.id}'
                rate=Status.objects.get(lesson=task)
                status={
                    'status':rate.status,
                    'rating':rate.rating,
                }
                data.append({
                    'id':task.id,
                    'name':task.name,
                    'file_name':task.file.name,
                    'file':url,
                    'description':task.description,
                    'status':status
                })
            return Response(data)
        except:
            return Response({"error":'Not Found'})
    
    

class SaveFile(APIView):
    def get(request,id):
         document=Lesson.objects.get(id=id)
         file = open(document.file.path, 'rb')
             # Return the file as a `FileResponse`
         response = FileResponse(file)
         return response

class AddedTask(APIView):
    permission_classes = [IsAdminUser]
    def post(self, requset):
        users=User.objects.all()
        data=requset.data
        task=Lesson.objects.create(
            name=data['name'],
            file=data.get('file'),
            description=data['description'],
            users=users
        )
        task.save()
        status=Status.objects.create(
            status="Berildi",
            rating=0.0,
            lesson=task
        )
        status.save()
        return Response({'response':'OK'})

class CreateUser(APIView):
    permission_classes = [TokenAuthentication]
    def post(self, request):
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
        
    

