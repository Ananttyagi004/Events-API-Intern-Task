from django.urls import path
from . import views

urlpatterns=[
    path('events/',views.EventList.as_view(),name='events'),
    path('post/',views.EventAdd.as_view(),name='addevent'),
    path('list/<int:pk>',views.EventDetail.as_view(),name='details')
]