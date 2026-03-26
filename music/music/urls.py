from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('genres', views.genres),
    path('tracks', views.tracks),
    path('artists/', views.artists),

    path('addgenre', views.add_genre),
    path('editgenre/<int:id_genre>', views.edit_genre),
    path('deletegenre/<int:id_genre>', views.delete_genre),

    path('addtrack', views.add_track),
    path('edittrack/<int:id_track>', views.edit_track),
    path('deletetrack/<int:id_track>', views.delete_track),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
