from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [
    path('profiles/', include(('profiles.urls', 'profiles'))),
]

urlpatterns += [
    path('authors/', include(('authors.urls', 'authors'))),
]

urlpatterns += [
    path('questions/', include(('questions.urls', 'questions'))),
]