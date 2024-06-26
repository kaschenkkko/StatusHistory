from api.views import ServiceViewSet, StatusHistoryViewSet, sla_calculation
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('services', ServiceViewSet)
router.register(r'history/(?P<service_id>.+)',
                StatusHistoryViewSet, basename='statushistory')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:service_id>/<str:start_date>/<str:end_date>/',
         sla_calculation),
    path('docs/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
