from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework import generics

from .models import Post,Comment
from .serializers import PostBaseModelSerializer, PostListModelSerializer, PostRetrieveModelSerializer, CommentListModelSerializer


#게시글 목록 + 생성
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):       #read
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.is_authenticated:           #로그인 된 경우
            serializer.save(writer=request.user)
        else:           
            serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#게시글 상세, 수정
class PostRetrieveUpdateView(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):       
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    def get_permissions(self):
        permission_classe = list()
        action = self.action
        if action =='list':
            permission_classe = [AllowAny]
        elif action in ['create','retrieve']:
            permission_classe = [IsAuthenticated]
        elif action in ['update','partial_update','destroy']:
            permission_classe = [IsAdminUser]

        return [permission() for permission in permission_classe]

        

    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk=None):
        post = self.get_object()        #불러오기
        comment_all = post.set_comment.set.all()
        serializer = CommentListModelSerializer(comment_all, many=True)
        return Response(serializer.data)



@api_view()
def calculator (request):
    # 1. 데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')

    # 2. 계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators == '-':
            result = int(num1) - int(num2)
        elif operators == '*':
            result = int(num1) * int(num2)
        elif operators == '/':
            result = int(num1) / int(num2)
        else:
            result = 0

        data = {
            'type' : 'FBV',
            'result' : result,
        }

    # 3. 응답
        return Response(data)


class CalculatorAPIView(APIView):
    def get(self, request):
        # 1. 데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')

    # 2. 계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators == '-':
            result = int(num1) - int(num2)
        elif operators == '*':
            result = int(num1) * int(num2)
        elif operators == '/':
            result = int(num1) / int(num2)
        else:
            result = 0

        data = {
            'type' : 'CBV',
            'method' : 'POST', 
            'result' : result,
        }
    # 3. 응답
        return Response(data)

    def post(self, request):
        pass