from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    User, UserSerializers,
    RegisterSerializer,
)
from rest_framework.permissions import IsAdminUser

# ----------------------------------
# UserView -> Full Control for permissions.IsAdminUser
# ----------------------------------
class UserView(ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializers
    permission_classes = (IsAdminUser,)
 

# ----------------------------------
# UserCreateView -> Only CreateUser for permissions.AllowAny
# ----------------------------------
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

class RegisterView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

