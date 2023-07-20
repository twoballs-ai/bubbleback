from django.db import models
#
# # Create your models here.
class Canvas(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Node(models.Model):
    canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='nodes')
    node_id = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    posX = models.IntegerField()
    posY = models.IntegerField()
    class Meta:
        verbose_name = 'Ноды'
        verbose_name_plural = 'Ноды'

    def __str__(self):
        return self.node_id


class Edge(models.Model):
    canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='edges')
    # source = models.CharField(max_length=100)
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_edges_source')

    # target = models.CharField(max_length=100)
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_edges_target')


    class Meta:
        verbose_name = 'Узлы'
        verbose_name_plural = 'Узлы'

    def __str__(self):
        return f"{self.source}-{self.target}"  
#
#
# class Node(models.Model):
#     canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='canvas_nodes')
#     node_id = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Ноды'
#         verbose_name_plural = 'Ноды'
#
#     def __str__(self):
#         return self.node_id
#
#
# class DataNode(models.Model):
#     node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='data')
#     label = models.CharField(max_length=100)
#     style = models.CharField(max_length=100)
#     link = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Данные для Ноды'
#         verbose_name_plural = 'Данные для Ноды'
#
#     def __str__(self):
#         return self.label
#
#
# class PositionNode(models.Model):
#     node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='position')
#     posX = models.IntegerField()
#     posY = models.IntegerField()
#
#     class Meta:
#         verbose_name = 'координаты Ноды'
#         verbose_name_plural = 'координаты Ноды'
#
#     def __str__(self):
#         return f"координаты для ноды - ({self.node}): x{self.posX}-y{self.posY}"
#
#
# class Edge(models.Model):
#     canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='canvas_edges')
#     edge_id = models.CharField(max_length=100)
#
#
#     class Meta:
#         verbose_name = 'Узлы'
#         verbose_name_plural = 'Узлы'
#
#     def __str__(self):
#         return self.edge_id
#
#
# class DataEdge(models.Model):
#     edge = models.ForeignKey(Edge, on_delete=models.CASCADE, related_name='edge_data')
#     source = models.CharField(max_length=100)
#     target = models.CharField(max_length=100)
#     label = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Данные для Узла'
#         verbose_name_plural = 'Данные для Узла'
#
#     def __str__(self):
#         return self.label