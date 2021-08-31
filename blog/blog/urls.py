from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from .sitemaps import CategorySitemaps, PostSitemaps

from core.views import frontpage, about, robots_txt

sitemaps = {'category': CategorySitemaps, 'post': PostSitemaps}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('start.urls')),
    path('', frontpage, name='frontpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
