from rest_framework import viewsets
from .models import Categoria, Transaccion
from .serializers import CategoriaSerializer, TransaccionSerializer
from django.db.models import Sum

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        categorias = Categoria.objects.all()
        filtro = self.request.GET.get('filter')
        
        if filtro == 'exceeds-limit':
            exceed_categories = self.filterCategoriaExceedLimit(categorias)
            return categorias.filter(pk__in = exceed_categories)
                
        if filtro == 'not-exceeds-limit':
            not_exceed_categories = self.filterCategoriaNotExceedLimit(categorias)
            return categorias.filter(pk__in = not_exceed_categories) 
           
        return categorias
    
    def filterCategoriaExceedLimit(self, categories):
        sum_amounts_by_category = Transaccion.objects.values('category_id').order_by('category_id').annotate(presupuesto=Sum('amount'))
        exceed_categories = []

        for cat in categories:
            sum_presupuesto = sum_amounts_by_category.get(category_id=cat.id)['presupuesto']
            if(sum_presupuesto > cat.limit):
                exceed_categories.append(cat.id)

        return exceed_categories


    def filterCategoriaNotExceedLimit(self, categories):
        sum_amounts_by_category = Transaccion.objects.values('category_id').order_by('category_id').annotate(presupuesto=Sum('amount'))
        not_exceed_categories = []
        
        for cat in categories:
            sum_presupuesto = sum_amounts_by_category.get(category_id=cat.id)['presupuesto']
            if(sum_presupuesto <= cat.limit):
                not_exceed_categories.append(cat.id)

        return not_exceed_categories

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer