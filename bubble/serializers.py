from rest_framework import serializers
from . import models




# class DataNodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DataNode
#         fields = ['id','label', 'link', 'style']
#
#         def __init__(self, *args, **kwargs):
#             super(DataNodeSerializer, self).__init__(*args, **kwargs)
#             request = self.context.get('request')
#             self.Meta.depth = 0
#             if request and request.method == 'GET':
#                 self.Meta.depth = 2
#
#
# class DataEdgeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DataEdge
#         fields = ['id','source', 'target','label']
#
#         def __init__(self, *args, **kwargs):
#             super(DataEdgeSerializer, self).__init__(*args, **kwargs)
#             request = self.context.get('request')
#             self.Meta.depth = 0
#             if request and request.method == 'GET':
#                 self.Meta.depth = 2
#
#
# class PositionNodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.PositionNode
#         fields = ['id','posX', 'posY']
#
#
# class NodeSerializer(serializers.ModelSerializer):
#     data = DataNodeSerializer(many=True)
#     position = PositionNodeSerializer(many=True)
#
#     class Meta:
#         model = models.Node
#         fields = ['id','node_id','data','position']
#
#         def __init__(self, *args, **kwargs):
#             super(NodeSerializer, self).__init__(*args, **kwargs)
#             request = self.context.get('request')
#             self.Meta.depth = 0
#             if request and request.method == 'GET':
#                 self.Meta.depth = 2
#
#
# class EdgeSerializer(serializers.ModelSerializer):
#     edge_data = DataEdgeSerializer(many=True)
#
#     class Meta:
#         model = models.Edge
#         fields = ['id','edge_id','edge_data']
#
#         def __init__(self, *args, **kwargs):
#             super(EdgeSerializer, self).__init__(*args, **kwargs)
#             request = self.context.get('request')
#             self.Meta.depth = 0
#             if request and request.method == 'GET':
#                 self.Meta.depth = 2
#

class Canvaserializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    # canvas_nodes = NodeSerializer(many=True)
    # canvas_edges = EdgeSerializer(many=True)
    class Meta:
        model = models.Canvas
        fields = ['id','title','nodes','edges']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(Canvaserializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1
