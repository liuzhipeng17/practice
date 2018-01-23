class ModelA(models.Model):
    name = models.CharField()


class ModelB(models.Model):
    f1 = models.CharField()
    model_a = models.ForeignKey(ModelA)


class ASerializer(serializers.ModelSerializer):
    model_b_ids = serializers.CharField()
    class Meta:
        model = ModelA
        #write_only_fields = ('model_b_ids',)# 记住，write_only_fields没有这个属性； read_only_fields可以允许这么写
		extra_kwargs = {
			'model_b_ids' : {'write_only': True}, # 或者直接在model_b_ids = serializer.CharField(write_only=True)
		}


class AView(CreateModelMixin, GenericViewSet):

    def perform_create(self, serializer): 
        model_b_ids = parse_somehow(serializer.validated_data["model_b_ids"])
        #do something...