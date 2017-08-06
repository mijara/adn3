from .models import Ticket


def validate_secret(email, secret):
    try:
        Ticket.objects.get(email=email, secret=secret)
        return True
    except Ticket.DoesNotExist:
        return False
