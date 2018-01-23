POST 请求---------> 反序列化过程------->
	deserializer: Json → native datatype【data = JSONParser().parse(BytesIO(content))】 →  isntance【serializer = SnippetSerializer(data=data)
	 serializer.is_valid()# True serializer.save()】
GET 请求 ----------> 序列化过程---------->
	serilization : isntance(django 模型实例) → native datatype（python 原生数据类型）【serializer.data】 → Json【JSONRenderer().render(serializer.data)】，将model实例的转为json格式response出去。
	从REST的设计原则看，它实际上是为了满足客户端的需求，现在的web后端与客户端（ios/android）打交道的多，这样的格式化response更便于它们解析。换句话说就是：将response打包成某种格式（如JSON)的东西。