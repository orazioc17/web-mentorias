from functools import reduce
from typing import Iterable

from django.db import models
from django.contrib.auth.models import User

from .helpers.constants import NUMERO_CALIFICACION, TIPO_CALIFICACION, EstudianteAMentor, MentorAEstudiante

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False, unique=True)
    descripcion = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre
        

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    costo_hora = models.DecimalField(decimal_places=2, max_digits=6)
    categorias = models.ManyToManyField(Categoria)
    calificacion_promedio = models.FloatField(null=True, blank=True, editable=False)

    def calificar(self, calificacion_mentor: int, estudiante_id: int, comentario: str = None):
        estudiante = Estudiante.objects.get(id=estudiante_id)
        Calificaciones.objects.create(
            mentor=self, estudiante=estudiante, calificacion=calificacion_mentor,
            comentario=comentario, tipo_calificacion=EstudianteAMentor
        )

        calificaciones = Calificaciones.objects.filter(mentor=self, tipo_calificacion=EstudianteAMentor)
        calificaciones_resultados = calificaciones.values_list('calificacion', flat=True)
        self.calificacion_promedio = (reduce(lambda x, y: x+y, calificaciones_resultados, 0)) / calificaciones.count()
        self.save()
    
    def __str__(self) -> str:
        return f'{self.user.username} - Mentor'


class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    calificacion_promedio = models.FloatField(null=True, blank=True, editable=False)

    def calificar(self, calificacion_estudiante: int, mentor_id: int, comentario: str = None):
        mentor = Mentor.objects.get(id=mentor_id)
        Calificaciones.objects.create(
            mentor=mentor, estudiante=self, calificacion=calificacion_estudiante,
            comentario=comentario, tipo_calificacion=MentorAEstudiante
        )

        calificaciones = Calificaciones.objects.filter(estudiante=self, tipo_calificacion=MentorAEstudiante)
        calificaciones_resultados = calificaciones.values_list('calificacion', flat=True)
        self.calificacion_promedio = (reduce(lambda x, y: x+y, calificaciones_resultados, 0)) / calificaciones.count()
        self.save()

    def __str__(self) -> str:
        return f'{self.user.username} - Estudiante'


class Calificaciones(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, editable=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, editable=False)
    calificacion = models.PositiveSmallIntegerField(choices=NUMERO_CALIFICACION, blank=False, null=False, editable=False)
    comentario = models.TextField(null=True, blank=True, editable=False)
    tipo_calificacion = models.CharField(max_length=50, choices=TIPO_CALIFICACION, null=False, blank=False, editable=False)

    def __str__(self) -> str:
        if self.tipo_calificacion == EstudianteAMentor:
            return f'Mentor [{self.mentor.user.username}] - {self.calificacion} estrellas'
        else:
            return f'Estudiante [{self.estudiante.user.username}] - {self.calificacion} estrellas'


# class Certificados(models.Model):
    
#     tipo_certificado = models.CharField(choices=)
