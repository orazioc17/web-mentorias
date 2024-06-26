# Generated by Django 4.0.10 on 2024-05-30 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_hora', models.DecimalField(decimal_places=2, max_digits=6)),
                ('calificacion_promedio', models.FloatField(blank=True, null=True)),
                ('categorias', models.ManyToManyField(to='perfiles.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('calificacion_promedio', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('tipo_calificacion', models.CharField(choices=[('MentorAEstudiante', 'Mentor a Estudiante'), ('EstudianteAMentor', 'Estudiante a Mentor')], max_length=50)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.estudiante')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.mentor')),
            ],
        ),
    ]
