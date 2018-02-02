# 如何设置请求的权限设置

# 下面是设置只有这个资源是资源拥有者才能执行的操作，比如删除文章，只能是作者才能删除，其他人删除不了。

# example1 只有是自己的资源，才允许修改

		# step1 定义权限

		from rest_framework import permissions

		class IsOwnerOrReadOnly(permissions.BasePermission):
			"""
			Object-level permission to only allow owners of an object to edit it.
			Assumes the model instance has an `owner` attribute.
			"""
			message = "only author can edit"  # 当用户没有这个权限的时候，会抛出异常，异常的消息可以自定，就是message的内容

			def has_object_permission(self, request, view, obj):
				# Read permissions are allowed to any request,
				# so we'll always allow GET, HEAD or OPTIONS requests.
				if request.method in permissions.SAFE_METHODS:
					return True

				# Instance must have an attribute named `owner`.
				return obj.owner == request.user	# obj.owner, 相应该成obj.user
				

			
		# step2， 如何使用这个权限
		class ExampleView(APIView):
			permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
			
		# 记住，         
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.


		
# example2 黑名单blackList，如果用户的ip在黑名单里面，他则不具备权限
		from rest_framework import permissions

		class BlacklistPermission(permissions.BasePermission):
			"""
			Global permission check for blacklisted IPs.
			"""
			message = "your IP is in blacklisted"
			
			def has_permission(self, request, view):
				ip_addr = request.META['REMOTE_ADDR']
				blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
				return not blacklisted