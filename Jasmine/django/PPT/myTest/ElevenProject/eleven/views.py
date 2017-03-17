from django.contrib.auth.models import User
from eleven.serializer import UserSerializer, MomentSerializer
from rest_framework import permissions
from rest_framework import viewsets
from eleven.models import Moment

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MomentViewSet(viewsets.ModelViewSet):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
