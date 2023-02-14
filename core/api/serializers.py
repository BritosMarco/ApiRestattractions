from rest_framework.serializers import ModelSerializer


from ..models import PontoTuristico
from attractions.api.serializers import AttractionsSerializer
from localization.api.serializers import LocalizationsSerializer
from commentreviews.api.serializers import CommentreviewsSerializer
from reviews.api.serializers import ReviewsSerializers
from attractions.models import Attractions
from localization.models import Address


# importa do models e coloca dentro de uma clas metta model e
# especifica os campos que serão serializados

"""
NestedRealtionship
#Não é usual mas posso adicionar um novo campos ao meu serializer
#Para isso usaremos SerializerMethodField 
#from rest_framework.fields import SerializerMethodField 
#descrição_completa = SerializerMethodField 
#def get_descrição_completa(self, obj)
 #   return '%$ - %$' % (obj.name, obj.description)
 ou
 @property
 #def get_descrição_completa2(self)
 #   return '%$ - %$' % (self.name, self.description)
 """


class PontoTuristicoSerializer(ModelSerializer):
    """CRINADO PORNTOS TURÍSITCOS E DEMMAIS OBJETOS AO MESMO TMEPO,
    EX: CRIA O POTO TURISTICO, CRIA AS ATRAÇÕES, CRIA A LIZALIZAÇÃO TUDO AO MESMO TEMPO"""

    #para que não se tornem campos obrigatorios preciso inserir read_only=True aceita uma lista vazia, 
    # mas não escreve no DB vem sempre uma lista vazia.
    attractions = AttractionsSerializer(many=True)
    address = LocalizationsSerializer()
    #comment = CommentreviewsSerializer(many=True, read_only=True)
    #reviews = ReviewsSerializers(many=True, read_only=True)
    class Meta:
        model = PontoTuristico
        fields = ['id', 'name', 'description', 'approved', 'picture', 'attractions', 'comment', 'address', 'reviews']
        read_only_fields = ['comment', 'reviews']
    
    def create_attractions(self, attractions, point):
        for attraction in attractions:
            at = Attractions.objects.create(**attraction)
            point.attractions.add(at)


    def create(self, validated_data):
        #a variavel attractions criada agora vem com todos os campos do pontos turisitco
        #  mais uma lista de lista das atrações
        #remove a chave attractions e endreço do validated_data
        attractions = validated_data['attractions']
        del validated_data['attractions']
        #criando endereço lembrando que ele é uma foreingkey não precisa criar função para for.
        address = validated_data['address']
        del validated_data['address']

        var_address = Address.objects.create(**address)
        point = PontoTuristico.objects.create(**validated_data)
        point.address = var_address
        #cria o ponto turistico na variavel point e chama a função que vai passar os pontos turisticos
        self.create_attractions(attractions, point)

         #passando o endereço para o ponto turístico
        
        #precisei inserir point.save após criar o endreço porque eu mudei o point.
        point.save()

        """FIM CRINADO PORNTOS TURÍSITCOS E DEMMAIS OBJETOS AO MESMO TMEPO,
        EX: CRIA O POTO TURISTICO, CRIA AS ATRAÇÕES, CRIA A LIZALIZAÇÃO TUDO AO MESMO TEMPO"""

        """CRIANDO O PONTRO TURISTICO E VINCULANDO
        HA UMA ATRAÇÃO OU LOZALIZAÇÃO JÁ ESXISTENTE NO BANCO DE DADOS"""
        return point
    
       

