from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("", views.home, name="braian"),
    path('about/', views.about, name='about'),
    path('landing/', views.landing_page, name='landing-page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
