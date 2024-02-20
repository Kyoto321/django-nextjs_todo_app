from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
]
"""

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='taken_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='taken_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]