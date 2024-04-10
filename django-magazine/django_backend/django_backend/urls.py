from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_backend import settings
from django_backend.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('', include("main.urls")),
    path('', include("articles.urls")),
    path('', include("about.urls")),
    path('', include("contacts.urls")),
    path('', include("vacaciens.urls")),
    path('', include("search.urls")),
    path("__debug__/", include("debug_toolbar.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
admin.site.site_header = "Серебряночка"