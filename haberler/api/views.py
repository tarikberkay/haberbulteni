from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import Article, Writer
from haberler.api.serializers import ArticleSerializer, WriterSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


# CLASS APIVIEW'LER 

class WriterListCreateAPIView(APIView):
    def get(self, request):
        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance
    
    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



## FUNCTİON METHOD ##

# @api_view(['GET', 'POST'])
# def makale_list_create_api_view(request):
    
#     if request.method == 'GET':
#         makaleler = Makale.objects.filter(aktif=True) #objeleri filtreleyen query set
#         serializer = MakaleSerializer(makaleler, many=True) 
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = MakaleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)






# @api_view(['GET', 'PUT', 'DELETE'])
# def makale_detail_api_view(request, pk):
#     try:
#         makale_instance = Makale.objects.get(pk=pk)
#     except Makale.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code': 404,
#                     'message': f'Böyle bir id ({pk}) ile ilgili makale bulunamadı.'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
        
#     if request.method == 'GET':
#         serializer = MakaleSerializer(makale_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = MakaleSerializer(makale_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         makale_instance.delete()
#         return Response(
#             {
#                 'işlem': {
#                     'code': 204,
#                     'message': f'({pk}) id numaralı makale silinmiştir.'
#                 }
#             },
#             status = status.HTTP_204_NO_CONTENT
#         )