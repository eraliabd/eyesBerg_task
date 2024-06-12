from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Logo, ConferenceSection
from .serializers import LogoSerializer, ConferenceSectionSerializer


class LogoListCreateView(ListCreateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    parser_classes = [FormParser, MultiPartParser]


class LogoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    parser_classes = [FormParser, MultiPartParser]


class ConferenceSectionListCreateView(ListCreateAPIView):
    queryset = ConferenceSection.objects.all()
    serializer_class = ConferenceSectionSerializer
    parser_classes = [FormParser, MultiPartParser]


class ConferenceSectionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ConferenceSection.objects.all()
    serializer_class = ConferenceSectionSerializer
    parser_classes = [FormParser, MultiPartParser]
