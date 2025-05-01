from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from services.routers.routers import router as services_router
from appointments.routers.routers import router as appointments_router
from banners.routers.routers import router as banners_router
from branches.routers.routers import router as branches_router
from categories.routers.routers import router as categories_router 
from gallery.routers.routers import router as gallery_router
from FAQs.routers.routers import router as faqs_router
from inquiries.routers.routers import router as inquiries_router
from pop_ups.routers.routers import router as pop_ups_router
from  social_media.routers.routers import router as social_media_router
from teams.routers.routers import router as teams_router

router= DefaultRouter()
router.registry.extend(services_router.registry)
router.registry.extend(appointments_router.registry)
router.registry.extend(banners_router.registry)
router.registry.extend(branches_router.registry)
router.registry.extend(categories_router.registry)
router.registry.extend(inquiries_router.registry)
router.registry.extend(gallery_router.registry)
router.registry.extend(faqs_router.registry)
router.registry.extend(pop_ups_router.registry)
router.registry.extend(social_media_router.registry)
router.registry.extend(teams_router.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="Lab Tech API",
      default_version='v1',
      description="Lab Tech Backend System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sarojkhawas952@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('api/', include('dashboard.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('chaining/', include('smart_selects.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
