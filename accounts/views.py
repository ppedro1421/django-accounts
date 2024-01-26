from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *


class RegisterUserView(GenericAPIView):
    serializer_class=RegisterUserSerializer

    def post(self, request: Request) -> Response:
        user_data = request.data
        serializers = self.serializer_class(data=user_data)

        if serializers.is_valid(raise_exception=True):
            user = serializers.create(serializers.data)

            return Response({'data': user, 'message': 'User created!'}, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
