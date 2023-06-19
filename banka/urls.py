from django.urls import path, include
from django.views.generic import RedirectView
from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('banka_app/', include('banka_app.urls')),
    path('', RedirectView.as_view(url='banka_app/')),
]

admin.autodiscover()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
