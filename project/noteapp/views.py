from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Page
from .serializers import PageSerializer



class PageViewSet(ModelViewSet):
    """Pageモデルの一覧、作成、更新、削除のAPI
    """
    serializer_class = PageSerializer
    #　ログイン済みの場合だけ許可
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        return Page.objects.filter(
            user=self.request.user,
        ).order_by('-updated_at', '-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)