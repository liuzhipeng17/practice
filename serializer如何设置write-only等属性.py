# write-only 属性的意思： 这个字段用户你可以提交上来，
# 也允许你update object 或者creat object,但是repsone回去的时候，不会有这个字段

# 比如用户Serializer的时候（password这个字段可以设置为write-only, 即不应该将password序列化回去给前端)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
		
# 更新，还需要注册验证码
class CreateUserSerializer(serializers.ModelSerializer):
	sms_code = models.CharFields()
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'sms_code')
        extra_kwargs = {'password': {'write_only': True}, 'sms_code': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
		
# 更新2 ，还需要用户确认二次密码
class CreateUserSerializer(serializers.ModelSerializer):
	password_confirm = models.CharFields()
	sms_code = models.CharFields()
    class Meta:
        model = User
        fields = ('email', 'username', 'password','sms_code', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}, 
						'sms_code': {'write_only': True}, 
						'password_confirm':{'write_only':True, validators:[]}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
		
# 更新3：
class RegisterSerializer(serializers.ModelSerializer):
    """
    注册的时候，需要注册用户手机号，填写验证码，填写密码，二次密码
    # required=True，说明在反序列化是，这个字段是必须要有的
    # write_only，说明在序列化时，不会有这个字段。即response到前端的时候，你不会得到这个字段
    # 当然，这些属性还可以在extra-kwargs设置

    """
    mobile = serializers.CharField(max_length=11, min_length=11,
                                   validators=[MobileTypeValidator(),
                                            UniqueValidator(
                                                queryset=user_model.objects.all(),
                                                message="The mobile has been registered"
                                   )])
    password = serializers.CharField(write_only=True, required=True, max_length=16, min_length=6)
    password_confirm = serializers.CharField(write_only=True, required=True,
                                             validators=[ConfirmPasswordValidator('password')])
    sms_code = serializers.CharField(required=True, validators=[SmsCodeValidator('mobile')])
	
	
# 更新4
mobile_regex = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
mobile_message = 'invalid mobile number, please try again'


class MobileTypeValidator(RegexValidator):

    def __init__(self):
        super(MobileTypeValidator, self).__init__(mobile_regex, mobile_message)
		
# 更新5 有Read_only_fields，
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_name', 'users', 'created')
        read_only_fields = ('account_name',)
		
# 当我们的model，如果field设置了属性editable=Fasle, serializers的时候会自动添加read_only=True,不需要手动增加
