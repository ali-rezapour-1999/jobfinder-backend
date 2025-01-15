from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserDeviceInfo


class DeviceInfoView(APIView):
    def post(self, request):
        data = request.data
        try:
            UserDeviceInfo.objects.create(
                browser=data.get("browser", ""),
                platform=data.get("platform", ""),
                language=data.get("language", ""),
                screen_resolution=data.get("screenResolution", ""),
                timezone=data.get("timezone", ""),
            )
            return Response(
                {"message": "Device info saved."}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
