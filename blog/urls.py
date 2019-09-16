
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
