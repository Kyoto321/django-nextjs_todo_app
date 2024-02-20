from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
User = get_user_model()


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        #data = self.request.data
        data = request.data

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)

                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})
