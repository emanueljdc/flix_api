
from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None

        # OU
        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0
        #     reviews_count = reviews.count()

        #     for review in reviews:
        #         sum_reviews += review.stars

        #     return round(sum_reviews/reviews_count, 1)
        # return None

# Exemplos de validação no Serialiazer

    def validate_release_data(self, value):
        if value.year < 2000:
            raise serializers.ValidationError('Não é possivel inserir filmes produzidos antes do ano 2000. Filme muito antigo')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O Resume não pode ter mais de 200 caracteres')
        return value