from django.urls import path, include
from games import views as games_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', games_views.index, name='home'),
    path('', include('games.urls')),
    path('', games_views.index.as_view(), name='home'),
    path('api/games/', games_views.tutorial_list),
    path('api/games/<int:pk>/', games_views.tutorial_detail),
    path('api/games/published/', games_views.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
