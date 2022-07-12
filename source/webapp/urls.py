from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, create_task, TaskView, delete_task, UpdateTask, RedirectView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('tasks/', RedirectView.as_view(pattern_name="index")),
    path("tasks/add/", create_task, name="create_task"),
    path("task/<int:pk>/", TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete', delete_task, name="delete_task"),

]
