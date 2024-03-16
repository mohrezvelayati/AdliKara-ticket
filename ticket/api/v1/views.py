from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from ticket.models import Ticket
from .serializers import TicketSerializer


# Create your views here.

class TicketCreateView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer