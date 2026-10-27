
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls') ),
    path('items/', include('item.urls') ),
    path('dashboard/', include('dashboard.urls') ),
    path('conversation/', include('conversation.urls') ),
    path('', include('API.urls') ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    
admin.site.site_header = "BuyKart Administration"    
admin.site.site_title = "BuyKart Admin Portal"       
admin.site.index_title = "Welcome to BuyKart Management"


handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_500_view'
handler403 = 'core.views.error_403_view'
handler400 = 'core.views.error_400_view'