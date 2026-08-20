from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardStatsAPIView(APIView):
    """Return the statistics currently displayed by the dashboard."""

    def get(self, request):
        return Response(
            {
                "user_count": 42,
                "sales": 999.99,
            }
        )
