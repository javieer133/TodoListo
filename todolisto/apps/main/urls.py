from django.urls import include, path
from apps.main.views import *
from django.contrib.auth import views as auth_views


# noinspection PyInterpreter
urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('tareas', tareas, name="tareas"),
    path('agregarTareas',agregarTarea, name="agregarTarea"),
    path(r'^$', cerrar, name='cerrar'),
    path(r'^tarea/(?P<tarea_id>\d+)/$', eliminarTarea, name="eliminarTarea"),
    path(r'^tareas/(?P<pk>\d+)/editar/$', EditarTarea.as_view(), name="editarTarea"),
    path('calendario', calendarView, name="calendario"),

]
