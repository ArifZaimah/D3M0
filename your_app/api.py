from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardStatsAPIView(APIView):
    """Return the statistics currently displayed by the dashboard."""

    @extend_schema(
        summary='Get dashboard statistics',
        responses=inline_serializer(
            name='DashboardStats',
            fields={
                'user_count': serializers.IntegerField(),
                'sales': serializers.FloatField(),
            },
        ),
    )
    def get(self, request):
        return Response(
            {
                'user_count': 42,
                'sales': 999.99,
            }
        )
