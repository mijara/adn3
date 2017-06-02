from .models import ReserveAttempt


def validate_secret(email, secret):
    print(email, secret)

    try:
        ReserveAttempt.objects.get(email=email, secret=secret)
        return True
    except ReserveAttempt.DoesNotExist:
        return False
