from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ImageUploadForm
from .compare_images import compare_images
from .serializers import ImageUploadSerializer
from .models import ImageModel
from django.shortcuts import render


@api_view(['GET', 'POST'])
def image_compare_api(request):
    if request.method == 'POST':
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            index = compare_images(image)
            if index == 400: #for other color without green
                return Response({'Please Enter Valid Green Image'})
            return Response({'Best matched image index': index}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return Response({'message': 'Please use POST to upload an image'}, status=status.HTTP_200_OK)


def home(request):
    images = ImageModel.objects.all()  # fetch images outside the if condition
    context = {'images': images}  # include images in context

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            index = compare_images(image)
            if index == 400:
                context['index'] = 'Not Green Leaf'
            else:
                context['index'] = index  # add index to context

    else:
        form = ImageUploadForm()
    context['form'] = form  # include the form in the context
    return render(request, 'home.html', context)
