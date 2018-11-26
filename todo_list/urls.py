from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('done/<list_id>', views.done, name="done"),
    path('undo/<list_id>', views.undo, name="undo"),
    path('edit/<list_id>', views.edit, name="edit")

]
