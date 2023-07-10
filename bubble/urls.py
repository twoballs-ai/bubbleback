from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bubble import views

urlpatterns = [
    # path('node/<int:pk>', views.NodeDetailView.as_view()),
    path('canvas/<int:pk>', views.CanvasDetailView.as_view()),
    path('node-list/<int:canvas_id>', views.CanvasNodeList.as_view()),
    path('node-detail/<int:canvas_id>/<str:id>', views.NodeDetailView.as_view()),
    path('edge-list/<int:canvas_id>', views.CanvasEdgeList.as_view()),
    path('edge-detail/<int:canvas_id>/<int:pk>', views.EdgeDetailView.as_view()),
    # path('canvas-nodes/<int:canvas_id>', views.CanvasNodeList.as_view()),
    # path('nodes/<int:pk>', views.NodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)