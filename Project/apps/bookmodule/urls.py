from . import views
from django.urls import path , include

urlpatterns = [
    path('',views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
]
