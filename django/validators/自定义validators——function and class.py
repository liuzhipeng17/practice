	# function based validator
	def validate_20mb_size(value):
		max_size = 1024 * 1024 * 20
		if value.size > max_size:
			raise serializers.ValidationError('profile Image is too large')
		
	# then we use like this
	profile_dict = serializers.ImageField(validators=[validate_20mb_size])

	# Class based validtor
	class ImageSizeValidtor(object):
		def __init__(self, max_size):
			self.max_size = 1024 * 1024 * max_size
			
		def __call__(self, value):
			if value.size > self.max_size:
				raise  serializers.ValidationError('profile Image is too large')

	# then we user like this
	profile_dict_c = serializers.ImageField(validators=[ImageSizeValidtor(max_size=20)])
	
	
	
# 下面主要将一下class的补充
from rest_framework.serializers import ValidationError

class EndDateValidator(object):
    def __init__(self, start_date_field):
        self.start_date_field = start_date_field

    def set_context(self, serializer_field):
        self.serializer_field = serializer_field	
		# 这里主要是获取self.serializer_field, 然后通过他得到serializer = self.serializer_field.parent
	

    def __call__(self, value):
        end_date = value
        serializer = self.serializer_field.parent
        raw_start_date = serializer.initial_data[self.start_date_field]

        try:
            start_date = serializer.fields[self.start_date_field].run_validation(raw_start_date)
        except ValidationError:
            return  # if start_date is incorrect we will omit validating range

        if start_date and end_date and end_date < start_date:
            raise ValidationError('{0} cannot be less than {1}'.format(self.serializer_field.field_name, self.start_date_field))
			
# 怎么使用（有两种方法）
# 第一种
	end_date = serializers.CharField(validators=[EndDateValidator('start_date')])
	
	
# 第二种
		class MyModelSerializer(serializers.ModelSerializer):
			end_date = serializer.CharField()
		
		class Meta:
			model = MyModel
			extra_kwargs = {"end_data": {"validators": [EndDateValidator('start_date'),]}}
			
			
# 附上官网关于class-based的例子
Class-based
To write a class-based validator, use the __call__ method. 
Class-based validators are useful as they allow you to parameterize and reuse behavior.

class MultipleOf(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            message = 'This field must be a multiple of %d.' % self.base
            raise serializers.ValidationError(message)
Using set_context()

In some advanced cases you might want a validator to be passed the serializer field it is being used with as additional context. 
You can do so by declaring a set_context method on a class-based validator.

def set_context(self, serializer_field):
    # Determine if this is an update or a create operation.
    # In `__call__` we can then use that information to modify the validation behavior.
    self.is_update = serializer_field.parent.instance is not None