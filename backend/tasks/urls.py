from django.urls import path
from .views import (
    ListTasksView,
    RetrieveTasksView, 
    SearchView, 
    CreateTaskAPIView,
    UpdateTasksView,
    DeleteAPIView
)

urlpatterns = [

    path('dashboard/', ListTasksView.as_view(), name='dashboard'),
    path('create-task/', CreateTaskAPIView.as_view(), name='create'),
    path('dashboard/<slug:slug>/', RetrieveTasksView.as_view(), name='tasks'),
    path('search/', SearchView.as_view(), name='search'),
    path('task/update/<slug:slug>/', UpdateTasksView.as_view(),name='update-task'),
    path('task/delete/<slug:slug>/', DeleteAPIView.as_view(), name='delete')
    #path('<pk>/dashboard/', RetrieveTasksView.as_view(), name='tasks')
]




