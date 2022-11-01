from django.contrib import admin
from django.urls import path
from .import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('cbvindex', views.TaskListView.as_view(), name='cbvindex'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvedit/<int:pk>', views.TaskUpdateview.as_view(), name='cbvedit'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete')
]
