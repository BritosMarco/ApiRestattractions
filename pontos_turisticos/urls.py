"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
# para manipular imagens  é necessário importar classes para manipulação de arquivos staticos.
from django.conf import settings
from django.conf.urls.static import static
# começando aparte de django_rest_Framwork
from rest_framework import routers
# implementando authenticação
from rest_framework.authtoken.views import obtain_auth_token


from core.api.viewsets import PontoTuristicoViewSet
from attractions.api.viewsets import AttractionsViewSet
from localization.api.viewsets import LocalizationsViewSet
from commentreviews.api.viewsets import CommentsViewSet
from reviews.api.viewsets import ReviewsViewSet

router = routers.DefaultRouter()  # define nossas rotas rest-framework
# registrando nossa rota de pontos turísticos
router.register(r'pontosturisticos', PontoTuristicoViewSet,
                basename='PontoTuristico')
# registrando nossa rota de atrações
router.register(r'attractions', AttractionsViewSet)
# registrando nossa rota de endereços
router.register(r'localization', LocalizationsViewSet)
# registrando nossa rota de comentários
router.register(r'comments', CommentsViewSet)
# registrando nossa rota de comentários
router.register(r'reviews', ReviewsViewSet)


urlpatterns = [
    # inclui todas as rotas dos nossos endpoints viewSet
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # endpoint para gerar token para autenticação
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
