from django.urls import path
from api.v1.tasks import views


urlpatterns = [
    path('', views.tasks),
    path("create/",views.create_task),
    path("update/<int:pk>/",views.update_task),
    path("delete/<int:pk>/",views.delete_task)
]