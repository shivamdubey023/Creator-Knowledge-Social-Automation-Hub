from rest_framework import generics
from .models import Knowledge
from .serializers import KnowledgeSerializers


class KnowledgeListCreateView(generics.ListCreateAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializers


class KnowledgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializers
