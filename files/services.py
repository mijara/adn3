from django.contrib.auth.models import User

from files.models import CourseFileDownload, CourseFile


def register_file_download(file: CourseFile, user: User):
    if user.is_anonymous:
        user = None

    CourseFileDownload.objects.create(file=file, user=user)
