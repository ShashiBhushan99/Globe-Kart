from tastypie.resources import ModelResource
from blog.models import Post
from tastypie.authorization import Authorization
class PostResource(ModelResource):
	class Meta:
		queryset=Post.objects.filter(title="shashi bhushan")
		resource_name='Post'
		authorization=Authorization()