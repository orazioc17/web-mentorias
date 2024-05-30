from django.contrib import admin

from .models import Mentor, Estudiante, Calificaciones, Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ['nombre', 'descripcion']


class MentorAdmin(admin.ModelAdmin):
    model = Mentor
    list_display = ['user', 'costo_hora', 'calificacion_promedio']
    readonly_fields = ['calificacion_promedio']
    sortable_by = ['calificacion_promedio']
    list_filter = ['categorias']
    search_fields = ['user__username']


class EstudianteAdmin(admin.ModelAdmin):
    model = Estudiante
    list_display = ['user', 'titulo', 'calificacion_promedio']
    readonly_fields = ['calificacion_promedio']
    sortable_by = ['calificacion_promedio']
    list_filter = ['titulo']
    search_fields = ['titulo']


class CalificacionesAdmin(admin.ModelAdmin):
    model = Calificaciones
    list_display = ['mentor', 'estudiante', 'calificacion', 'comentario', 'tipo_calificacion']
    readonly_fields = ['mentor', 'estudiante', 'calificacion', 'comentario', 'tipo_calificacion']
    list_display_links = ['calificacion']
    list_filter = ['tipo_calificacion', 'calificacion']
    sortable_by = ['calificacion']
    


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Calificaciones, CalificacionesAdmin)
