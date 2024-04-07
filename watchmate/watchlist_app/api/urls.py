
from django.urls import path,include
from .views import Movies_list,Movie_Update_Delete


urlpatterns = [
    
    
    path('create/', Movies_list.as_view(), name='create_movie'),
    path('update/<int:pk>/', Movie_Update_Delete.as_view(), name='movie_update'),
    
]
