import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    The main vieweset for viewing, editing, creating, and deleting account
    objects.
    """
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            account = Account.objects.create_user(
                serializer.data.get('email'),
                serializer.data.get('password'),
                username=serializer.data.get('username'),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        context = {
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    """
    View for logging a user in.
    """
    def post(self, request, format=None):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                context = {
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }

                return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        context = {
            'status': 'Unauthorized',
            'message': 'Username/password combination invalid.'
        }

        return Response(context, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    """
    View for logging a user out.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
