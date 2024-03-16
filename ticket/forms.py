from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["full_name", "bussiness", "email", "phone", "message", "created_date"]