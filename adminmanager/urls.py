 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
     path('',views.dashboard),
      path('category/',views.category),
        path('subcategory/',views.subcategory), 
        path('subcategoryById/',views.subcategoryById),
    path('products/',views.products),
    path('settings/',views.settings),
    path('homesettings/',views.homesettings),
     path('baner/',views.baner),
      path('banerupdate/',views.banerupdate),
       path('banerdelete/',views.banerdelete),
 path('newproduct/',views.newproduct),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
