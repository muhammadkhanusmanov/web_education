from rest_framework.views import APIView
from rest_framework.response import Response#FileResponse
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from .serilezer import LessonSerializer
from .models import Lesson
from django.http import FileResponse



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
            tasks=Lesson.objects.filter(users=user)
            data=[]
            for task in tasks:
                url=f'http://127.0.0.1:8000/home/{task.id}'
                data.append({
                    'id':task.id,
                    'name':task.name,
                    'file_name':task.file.name,
                    'file':url,
                    'description':task.description
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
    

