from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login, authenticate
from .models import Account

# Create your views here.
class AccountList(APIView):
    #Serializador para la Clase
    serializer_class = AccountSerializer
    #Permiso para la Clase
    #Lo tengo como politica global ahora settings.py
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        #No es necesario si configuro todo el APIView arriba or por settings.py
        #if not request.user.is_authenticated:
        #    return Response(status=status.HTTP_401_UNAUTHORIZED)

        accounts = Account.objects.all()
        serializer = self.serializer_class(accounts, many=True)
        return Response(serializer.data)

class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthLogin(APIView):
    ''' Manual implementation of login method '''

    #Por ahora no llamo a este metodo pa que?!
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)
        # Generate token and add it to the response object
        if account is not None:
            login(request, account)
            return Response({
                'status': 'Successful',
                'message': 'You have successfully been logged into your account.'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'Unauthorized', 
            'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)
