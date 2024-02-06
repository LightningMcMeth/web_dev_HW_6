from django.urls import path
from hw_6 import views

urlpatterns = [
    #path("entity", views.sendAll, name='all_messages'),
    path('entities/', views.listAllEntities, name='listAllEntities'),
    path('entities/<str:id>/', views.getEntityById, name='getEntityById'),
    path('deleteEntity/<str:id>', views.deleteEntityById, name='deleteEntityById'),
    path('createEntity/', views.createEntity, name='createEntity'),
]