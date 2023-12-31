from django.urls import path
from webapp.views import index_view, task_create_view, task_delete_view, task_view, task_update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', task_create_view, name='task_create'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('task/<int:pk>/update/', task_update_view, name='task_update_view'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete_view')
]
