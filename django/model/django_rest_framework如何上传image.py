def get_image_path(instance, filename):
    """
    Puts image in MEDIA_ROOT/photos/instance_id/file
    """
    return 'orders/%s/%s' % (instance.id, filename)

class PhotoOrder(models.Model):
    photo = models.ImageField(upload_to=get_image_path)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=110)
serializers.py

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoOrder

    def create(self, validated_data):
        return PhotoOrder.objects.create(**validated_data)
views.py

class OrderList(CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
		


