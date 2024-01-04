import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_tracking.mixins import LoggingMixin
from datetime import datetime

from core.models import *
from core.serializers import *


logger = logging.getLogger(__name__)


class CartoesViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartoesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    @action(detail=False, methods=['post'])
    def file(self, request):
        file_content = request.FILES.get('file')  # Lembrando que o arquivo enviando pelo front ou na requisição deve ser "file" utilizei o insonmia para envio 
        
        if file_content:
            lines = file_content.read().decode().split("\n")
            
           #Criação do cabeçalho para todos os dados que vierem dentro do arquivo
            header_info = {
                "nome": lines[0][0:29].strip(),
                "data": datetime.strptime(lines[0][29:37], '%Y%m%d').strftime('%Y-%m-%d'),
                "lote": lines[0][37:45].strip(),
                "qtd_registro": int(lines[0][45:51].strip()) 
            }

            extracted_data = []
            #Bloco for com numeração das linhas
            for index, line in enumerate(lines[1:], start=1):
                line = line.strip()
                #Permito a criação apenas da qtd de registro
                if line and index <= header_info["qtd_registro"]:
                    current_entry = {
                        "identificador_linha": line[0:3].strip(),
                        "numero_lote": line[3:7].strip(),
                        "numero": line[7:26].strip(),
                    }
                    extracted_data.append(current_entry)
            #Percorro todo "data"
            for data in extracted_data:
                #Crio e salvo meu objeto
                Cartoes.objects.create(
                    identificador_linha=data['identificador_linha'],
                    numero_lote=data['numero_lote'],
                    numero=data['numero'],
                    nome=header_info['nome'],
                    data=header_info['data'],
                    lote=header_info['lote'],
                    qtd_registro=header_info['qtd_registro']
                )

            return Response({'message': 'Dados processados e salvos com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Nenhum arquivo fornecido'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def consulta_numero(self, request):
        numero = request.query_params.get('numero')
        
        if numero:
            cartoes_encontrados = Cartoes.objects.filter(numero=numero)
            if cartoes_encontrados.exists():
                identificadores = [cartao.id for cartao in cartoes_encontrados]
                return Response({'identificadores': identificadores}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Nenhum cartão encontrado para o número fornecido'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Parâmetro "numero" não fornecido'}, status=status.HTTP_400_BAD_REQUEST)