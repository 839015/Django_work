from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializer import ProductModelSerializer
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.permissions import AllowAny


class ProductOperations(ModelViewSet):  # methods called overiding
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    #permission_classes = (AllowAny)

    def create(self, request, *args, **kwargs):
        jsonbody = request.data
        price = jsonbody.get('price')
        if price <= 0:
            return HttpResponse('Invalid Price.')
        return super().create(request, *args, **kwargs)  # The super() function is used to give access to methods and
        # properties of a parent or sibling class. The super() function returns an object that represents
        # the parent class.

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
