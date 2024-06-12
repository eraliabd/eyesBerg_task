from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    parser_classes = [FormParser, MultiPartParser]


class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all().filter(is_superuser=False)
    serializer_class = CustomUserSerializer


class CustomUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    parser_classes = [FormParser, MultiPartParser]
