from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
import logging

logger = logging.getLogger(__name__)

class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        logger.debug(f"Customers QuerySet: {customers}")
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)




