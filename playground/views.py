from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


class ShowDuplicatesView(generic.View):
    def get(self, request):
        users = User.objects.all()
        total = users.count()
        current = 0
        duplicates = []
        for user1 in users:
            print(f"Progress: {current / total * 100}%")
            current += 1
            for user2 in users:
                if user1 != user2:
                    ratio = similar(user1.username, user2.username)
                    if ratio > 0.95:
                        duplicates.append(f"{user1.username} - {user2.username} | {ratio}")

        return render(request, 'playground/show_duplicates.html', {'list': duplicates})
