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

    def __unicode__(self):
        return self.file.name
