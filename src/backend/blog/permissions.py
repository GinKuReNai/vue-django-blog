from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """オーナーのみアクセス権の許可(User)"""
    message = '他のユーザーを削除することはできません。' 
    
    def has_object_permission(self, request, view, obj):
        """GET, HEAD, OPTIONSは常に許可"""
        if request.method in SAFE_METHODS:
            return True
        print(obj, request.user)
        # 所有者のみすべて許可
        return obj == request.user

class IsOwnerOrReadOnly(BasePermission):
    """オーナーのみアクセス権の許可(Post)"""
    message = 'このオブジェクトのオーナーである必要があります。'
    
    def has_object_permission(self, request, view, obj):
        """GET, HEAD, OPTIONSは常に許可"""
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
