from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse

from .serializers import CanvasSerializer, EdgeSerializer,  NodeSerializer


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
    queryset = models.Node.objects.all()
    serializer_class = NodeSerializer
    lookup_field = 'id'


class CanvasEdgeList(generics.ListCreateAPIView):
    # queryset = models.Node.objects.all()
    serializer_class = EdgeSerializer

    def get_queryset(self):
        canvas_id = self.kwargs['canvas_id']
        canvas = models.Canvas.objects.get(pk=canvas_id)
        return models.Edge.objects.filter(canvas=canvas)


class EdgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Edge.objects.all()
    serializer_class = EdgeSerializer

#
# class CanvasNodeList(generics.ListCreateAPIView):
#     serializer_class = NodeSerializer
#
#     def get_queryset(self):
#         canvas_id = self.kwargs['canvas_id']
#         canvas = models.Canvas.objects.get(pk=canvas_id)
#         return models.Node.objects.filter(canvas=canvas)
#
#
# class NodeDetail(generics.ListCreateAPIView):
#     queryset = models.Node.objects.all()
#     serializer_class = NodeSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         node_id = models.Canvas.objects.get(pk=pk)
#         return models.Node.objects.filter(node_id=node_id)
#
#
# # class DataNodeDetail(generics.ListCreateAPIView):
# #     queryset = models.DataNode.objects.all()
# #     serializer_class = NodeSerializer
