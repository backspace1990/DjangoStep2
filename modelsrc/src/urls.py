from django.contrib import admin
from django.urls import path, include
from homeApp.views import homeapp_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeapp_view, name='home'),
    path('post/', include('post.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
