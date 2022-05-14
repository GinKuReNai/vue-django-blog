from django.shotcuts import get_object_or_404
from blog.models import Post

class MultipleFieldLookupMixin(object):
    """slug, idによってCommentをフィルタリングするMixin"""
    
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        # for field in self.lookup_fields:
            # if self.kwargs[field]:
                # filter[field] = self.kwargs[field]
        post_id = Post.objects.get(slug=self.kwargs['slug']).id
        filter['post'] = post_id
        filter['id'] = self.kwargs['id']
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj