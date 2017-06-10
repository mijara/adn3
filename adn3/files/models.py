from django.db import models


class CourseFile(models.Model):
    # related course.
    course = models.ForeignKey('courses.Course')

    # user friendly name.
    name = models.CharField(max_length=256, verbose_name='Nombre')

    # main file.
    file = models.FileField(verbose_name='Archivo')

    # count of downloads.
    downloads = models.IntegerField(default=0, verbose_name='Descargas')

    # stamps the date and time of upload.
    create_date = models.DateTimeField(auto_now_add=True)

    # stamps the date and time of update.
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'files:coursefile_detail', [self.course.pk, self.pk]

    @models.permalink
    def get_download_url(self):
        return 'files:coursefile_download', [self.course.pk, self.pk]

    @models.permalink
    def get_update_url(self):
        return 'files:coursefile_update', [self.course.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'files:coursefile_delete', [self.course.pk, self.pk]
