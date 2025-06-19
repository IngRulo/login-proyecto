from django.contrib import admin
from django.urls import path
from loginapp.views import login_view  # Importa tu vista de login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', login_view, name='home'),  # La raíz muestra el login
]