from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def contact_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            cont = Contact.objects.get(id=id)
            serializer = ContactSerializer(cont)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        cont = Contact.objects.all()
        serializer = ContactSerializer(cont, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ContactSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
