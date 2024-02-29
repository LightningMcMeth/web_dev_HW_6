from django.urls import path, re_path
from hw_6 import views

urlpatterns = [
    path('/', views.mainPage, name="mainPage"),
    path('entities/', views.listAllEntities, name='listAllEntities'),
    path('entities/<str:id>/', views.getEntityById, name='getEntityById'),
    path('deleteEntity/<str:id>', views.deleteEntityById, name='deleteEntityById'),
    path('createEntity/', views.createEntity, name='createEntity'),
    path('displayImage/', views.displayImage, name='displayImage'),
    re_path('.*', views.wrongUrl),
]