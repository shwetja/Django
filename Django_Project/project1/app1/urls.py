from django.urls import path
from . import views

urlpatterns =[
    path('add/', views.SimpleClassBasedView.as_view(), name='add_url'),
    path('show/', views.Studentview.as_view(), name='show_url'),
    path('update/<int:pk>/', views.Updateview.as_view(), name='update_url'),
    path('delete/<int:pk>/', views.Deleteview.as_view(), name='delete_url'),
]