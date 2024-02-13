from rest_framework import serializers 
from haberler.models import Article, Writer

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince 



# MODEL SERIALIZER #
class ArticleSerializer(serializers.ModelSerializer):
    
    time_since_pub = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = WriterSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        #fields = ['author', 'title', 'text']  #İlgili objeleri getirir. 
        #exclude = ['author', 'title', 'text']  #Bunun haricindekileri sırala demek için kullanılır.
        read_only_fields = ['id', 'creation_date', 'updated_date']  # sadece okunacakları belirlemek için kullanılır.

    def  get_time_since_pub(self,object):
        now = datetime.now()
        pub_date = object.published_date
        if object.active == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Aktif Degil!'
    
    def validate_published_date(self, date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olamaz!')
        return date_value



class WriterSerializer(serializers.ModelSerializer):
    
    # articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail',
    )
    
    class Meta:
        model = Writer
        fields = '__all__'





# STANDART SERIALIZER #
class ArticleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title  = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    published_date = serializers.DateField()
    active = serializers.BooleanField()
    creation_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)


    def create (self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance 

def validate(self, data):
    if data['title '] == data['description']:
        raise serializers.ValidationError('Başlık ve açıklama alanları aynı olamaz. Lütfen farklı bir açıklama giriniz.')
    return data

def validate_title(self, value):
    if len(value) < 20:
        raise serializers.ValidationError('başlık karakteri {len(value)} karakter içeriyor. Lütfen en az 20 karakter olacak şekilde ayarlayınız.')
    return value