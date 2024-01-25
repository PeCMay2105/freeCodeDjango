from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:course_id>/pagina_curso/",views.pagCurso,name="pagina_curso"),
    path("<int:Professor_id>/professor/",views.professor,name="professor")

]