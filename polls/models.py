from django.db import models
from django.urls import reverse_lazy


class Poll(models.Model):
    course = models.ForeignKey(
        'courses.Course',
        verbose_name='Curso'
    )

    student = models.ForeignKey(
        'registration.Student',
        verbose_name='Estudiante'
    )

    first = models.CharField(
        verbose_name='1.- ¿Ud. había usado antes algún software matemático o estadístico?',
        max_length=32,
        choices=(
            ('Sí', 'Sí'),
            ('No', 'No')
        )
    )

    second = models.IntegerField(
        verbose_name='2.- ¿A cuantas sesiones de laboratorio computacional asistió?',
    )

    third = models.CharField(
        verbose_name='3.- El material de instrucción le pareció :',
        max_length=32,
        choices=(
            ('Muy complicado', 'Muy complicado'),
            ('Complicado', 'Complicado'),
            ('Amigable', 'Amigable'),
            ('Muy Amigable', 'Muy Amigable'),
        )
    )

    fourth = models.CharField(
        verbose_name='4.- La presentación del material de instrucción le pareció:',
        max_length=32,
        choices=(
            ('Inadecuado', 'Inadecuado'),
            ('Poco adecuado', 'Poco adecuado'),
            ('Adecuado', 'Adecuado'),
            ('Muy adecuado', 'Muy adecuado'),
        )
    )

    fifth = models.CharField(
        verbose_name='5.- El material de instrucción respecto de las clases teóricas fue:',
        max_length=32,
        choices=(
            ('Muy atrasado', 'Muy atrasado'),
            ('Atrasado', 'Atrasado'),
            ('A Tiempo', 'A Tiempo'),
            ('Adelantado', 'Adelantado'),
        )
    )

    sixth = models.CharField(
        verbose_name='6.- La ayuda del ayudante de laboratorio le pareció:',
        max_length=32,
        choices=(
            ('Escasa', 'Escasa'),
            ('Buena', 'Buena'),
            ('Muy Buena', 'Muy Buena'),
        )
    )

    seventh = models.CharField(
        verbose_name='7.- ¿Fueron atendidas a tiempo sus consultas e inquietudes por el ayudante coordinador?',
        max_length=32,
        choices=(
            ('Sí', 'Sí'),
            ('No', 'No'),
        )
    )

    eighth = models.CharField(
        verbose_name='8.- El tiempo disponible en cada sesión es:',
        max_length=32,
        choices=(
            ('Muy corto', 'Muy corto'),
            ('Corto', 'Corto'),
            ('Normal', 'Normal'),
            ('Excesivo', 'Excesivo'),
        )
    )

    ninth = models.CharField(
        verbose_name='9.- Las instalaciones del laboratorio le parecen:',
        max_length=32,
        choices=(
            ('Incómodas', 'Incómodas'),
            ('Cómodas', 'Cómodas'),
            ('Muy Cómodas', 'Muy Cómodas'),
        )
    )

    tenth = models.CharField(
        verbose_name='10.- ¿Cuantas sesiones a la semana considera necesarias?',
        max_length=32,
        choices=(
            ('Una', 'Una'),
            ('Dos', 'Dos'),
            ('Una Quincenal', 'Una Quincenal'),
        )
    )

    eleventh = models.CharField(
        verbose_name='11.- Los preinformes (para entender la sesión) son:',
        max_length=32,
        choices=(
            ('Inútiles', 'Inútiles'),
            ('Poco útiles', 'Poco útiles'),
            ('Útiles', 'Útiles'),
            ('Muy Útiles', 'Muy Útiles'),
        )
    )

    twelfth = models.CharField(
        verbose_name='12.- Los controles le parecieron:',
        max_length=32,
        choices=(
            ('Muy difíciles', 'Muy difíciles'),
            ('Difíciles', 'Difíciles'),
            ('Adecuados', 'Adecuados'),
            ('Fáciles', 'Fáciles'),
        )
    )

    thirteenth = models.CharField(
        verbose_name='13.- El “sistema Aula” para la sesión le parece:',
        max_length=32,
        choices=(
            ('Poco adecuado', 'Poco adecuado'),
            ('Adecuado', 'Adecuado'),
            ('Inadecuado', 'Inadecuado'),
        )
    )

    fourteenth = models.CharField(
        verbose_name='14.- El “sistema Aula” para controles le parece:',
        max_length=32,
        choices=(
            ('Muy complicado', 'Muy complicado'),
            ('Complicado', 'Complicado'),
            ('Bueno', 'Bueno'),
            ('Muy Bueno', 'Muy Bueno'),
        )
    )

    fifteenth = models.CharField(
        verbose_name='15.- Globalmente la experiencia del laboratorio fue:',
        max_length=32,
        choices=(
            ('Inútil', 'Inútil'),
            ('Poco Útil', 'Poco Útil'),
            ('Útil', 'Útil'),
            ('Muy Útil', 'Muy Útil'),
        )
    )

    sixteenth = models.CharField(
        verbose_name='16.- Usted quisiera experimentar por su propia cuenta con el software en horarios distintos al de la sesión:',
        max_length=32,
        choices=(
            ('Sí', 'Sí'),
            ('No', 'No'),
        )
    )

    seventeenth = models.CharField(
        verbose_name='17.- Usted hubiese preferido trabajar en cada sesión: ',
        max_length=32,
        choices=(
            ('Sólo', 'Sólo'),
            ('Con Otro Alumno', 'Con Otro Alumno'),
            ('Me da Igual', 'Me da Igual'),
        )
    )

    eighteenth = models.TextField(
        verbose_name='18.- Comentarios y sugerencias:',
    )

    def get_absolute_url(self):
        return reverse_lazy('polls:poll_detail', args=[self.course.pk, self.pk])
