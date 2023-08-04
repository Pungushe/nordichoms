from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import path, include

urlpatterns = [
  # главная страница
  path('', include('core.urls')),
  # корзина
  path('cart/', include('cart.urls')),
  # заказ
  path('order/', include('order.urls')),

  # admin
  path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
