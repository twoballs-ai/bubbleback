from django.shortcuts import render
from . import models
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# Create your views here.
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .serializers import BlocksSerializer, CanvasSerializer, EdgeSerializer,  NodeSerializer, PostSerializer
from rest_framework.parsers import JSONParser

class CanvasDetailView(generics.RetrieveAPIView):
    queryset = models.Canvas.objects.all()
    serializer_class = CanvasSerializer


class CanvasNodeList(generics.ListCreateAPIView):
    # queryset = models.Node.objects.all()
    serializer_class = NodeSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Node.objects.filter(canvas=canvas)


class NodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Node.objects.filter(canvas=canvas)


class CanvasEdgeList(generics.ListCreateAPIView):
    # queryset = models.Node.objects.all()
    serializer_class = EdgeSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Edge.objects.filter(canvas=canvas)


class EdgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EdgeSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Edge.objects.filter(canvas=canvas)



# @csrf_exempt
# def save_post(request):
#     body_unicode = request.body.decode('utf-8')
    
#     data = json.loads(body_unicode)
#     lesson_id = data['lesson']
#     length = len(data['blocks'])
#     print(data)
#     # tom = models.Post.objects.get()
#     post_obj = models.Post.objects.create(lesson_id=int(lesson_id), blocks_count=length)
#     for i in range(length):
#         models.Block.objects.create(post_id = post_obj.id, id = data['blocks'][i]['id'],type = data['blocks'][i]['type'],data = data['blocks'][i]['data'])
#     return JsonResponse({'succesfull':'true'})


class CanvasPostList(generics.ListCreateAPIView):
    # queryset = models.Node.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Post.objects.filter(canvas=canvas)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer



class PostBlocksList(generics.ListCreateAPIView):
    # queryset = models.Node.objects.all()
    serializer_class = BlocksSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = models.Post.objects.get(pk=post_id)
        return models.Block.objects.filter(post=post)
