from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,  BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from django.http.response  import HttpResponse
import requests

# Implementado SearchField
from rest_framework.filters import SearchFilter

# implementado autenticação por endpoint
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

# importamos de ModelViewSet que compila todas as classes de CRUD
""" class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): 
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """


class PontoTuristicoViewSet(ModelViewSet):

    # faz uma requisição e pega todos os dados do DB
    # queryset = PontoTuristico.objects.all()

    # serializa(JSON) os dados que vieram do banco
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #parser_classes = [JSONParser] ## retorna um dicionário de JSON
    serializer_class = PontoTuristicoSerializer
    # Implementado necessidade de autenticação para acessar o endpoint
    permission_classes = (IsAuthenticated, IsAdminUser, )
    authentication_classes = (TokenAuthentication,)

    """
    # Temos mais possibilidade de gerir as  permissões segue 2 exemplos
    # permission_classes = (IsAuthenticatedOrOnly,) # permtie apenas GET quando não autenticado
    # permission_classes = (DjangoModelPermissions,) # podemos gerir as permissões pelo admin 
    # permission_classes = (DjangoObjectPermissions,) Permissões por objeto
    """

    """ Para filtrar minha queryset para trazer do banco apenas objetos
    que atendam alguma condição eu acesso o method get_queryset
    que herda de ModelViewSet(F12)/GenericViewSet(F12)/GenericAPIView(F12)/def get_queryset
    """
    """
    Posso usar def get_queryset para customizar o retornos do objeto do db usando filtros ou não
    2. implemento a def abaixo  filtrando e posso passar vários parametors de filtragem ou all para tornar todos objetos
    3. preciso informa o basename do meu model: PontoTuristico na url pois uma vez que
    apaguei a queryset genérica ele não identifica mais o Model utilizado.
    """

    def get_queryset(self):
        # AULA 6 IMPLEMENTANDO FILTROS (FILTERS)  DE FORMA MAIS HARDCODED
        ''' id = self.request.query_params.[''] ele é um dicionário posso passar assim.
        # entretanto  seria obritaório passar o id ,
        #se a pessoa não passar o id retorna Erro. por  isso é melhor 
        # mplementar com Get assikm não será obrigatório informar o id '''

        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        # lazyload, não pega todos os objetos apenas define a queryset
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if name:
            queryset = queryset.filter(name=name)
        if description:
            queryset = queryset.filter(description=description)


        return queryset
          # objeto filtrado

        # retorna todos objetos do banco
        # return PontoTuristico.objects.all()

     # FIM AULA 6 IMPLEMENTANDO FILTROS DE FORMA MAIS HARDCODED

     # AULA 7 IMPLEMENTANDO FILTROS (DJANGOFILTERBACKEND) DE FORMA MAIS HARDCODED
     # INSTALANDO A BIBLIOTECA PIP INSTALL DJANGOFILTER

    # AULA 8 IMPLEMENTADO SEARCHFIELD
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'Address__address1')
    # FIM AULA 8 IMPLEMENTADO SEARCHFIELD

    # AULA 9 IMPLEMENTADO LOOKUP_FIELD
    # muda o comportamento nativo do Django que busca um objeto pelo ID, vc pode customizar e determinar
    # o parâmetro de busca do objeto.
    # lookup_field = 'name'  # precisa ser único para garantir a integridade do DB
    # FIM AULA 9 IMPLEMENTADO LOOKUP_FIELD

    # **kwargs ´e um dicionário que normanelente tras {'pk': id}
    # *args é o tipo. Exemplo tuple
    # request.data(é o payload da minha request com todos os recursos passados)
    # def list para customizar sobrescrevendo a action
    # de GET do method list retorna uma lista com 1 ou mais objetos

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # def create para customizar sobrescrevendo a action de POST do method create
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # def destroy para customizar sobrescrevendo a action de DELETE do method destroy
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # def retrieve para customizar sobrescrevendo a action de GET do method retrieve
    # passando um argumento id para apenas um objeto e não uma lista como o method list.
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

     # def update para customizar sobrescrevendo a action de PUT do method update
    # passando um argumento id atualizar um objeto inteiro.
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # def partial_update para customizar sobrescrevendo a action de PATCH do method partial_update
    # passando um argumento id para atualizar parcialmente um objeto, ex. um ou dois campos.
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    ''' action personalizada para denunciar um ponto turístico, não é nativa do django eu criei.
     vou usar um decorators neste caso o action django preciso estudar o que é o action.
     tenho que importar do REST_FRAMEWORK
     O ACTIONS recebe como parametro os methods que vc quer que
     seja diparada ex. eu qeuro que seja seja disparada somente no GET
     preciso informar o detail prar ele pegar a pk caso contrário ele apontara para o endpoint inteiro.
     para acessar esse method no browser "endereco/id/complaint '''

    @action(methods=['get'], detail=True)
    def complaint(self, request, pk):
        pontoTuristico = get_list_or_404(PontoTuristico, id=pk)
        pontoTuristico = pontoTuristico[0]
        data = PontoTuristicoSerializer(pontoTuristico).data
        return Response(data, status=status.HTTP_200_OK)
    

    #method criado para atualizar o ponto turistico com uma atrvação que já existe no banco de dados
    # a URL será http://127.0.0.1:8000/pontosturisticos/1/association_attraction/

    @action(methods=['post'], detail=True)
    def association_attraction(self, request, pk):
        attractions = request.data['ids']
        point= PontoTuristico.objects.get(id=pk)

        point.attractions.set(attractions)

        point.save()

        return HttpResponse('Ok')
