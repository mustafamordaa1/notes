from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Note
from .serializers import NoteSerializer, UserSerializer, RegisterSerializer
from .filters import NoteFilter
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Register API
class RegisterAPI(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.AllowAny,)

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def main(request):
    if request.method == 'GET':
        notes = Note.objects.filter(author=request.user)
        filterset = NoteFilter(request.GET, queryset=notes)
        if filterset.is_valid():
            notes = filterset.qs
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'DELETE':
        notes = Note.objects.filter(author=request.user)
        filterset = NoteFilter(request.GET, queryset=notes)
        if filterset.is_valid() and notes:
            notes = filterset.qs
            notes.delete()
            return Response("Done")
        else:
            return Response("an Error has occured")

    elif request.method == 'POST':
        data = request.data
        data[0]['author'] = request.user.id
        serializer = NoteSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

