from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer
from .es import Grab, Camera


class WebGrab(APIView):
    """ provides back end support for webGRAB photo import app"""

    @staticmethod
    def get(request):
        """ """
        route = request.GET["id"]
        # returns a tuple of folders from 'parent' directory
        if route == 'destinations':
            return Response(Grab.get_destination_folders())
        # attempts to connect to camera. Returns True if successful. False if not
        if route == 'connect':
            camera = Camera()
            print(f'about to return {camera.response}')
            return Response(camera.response)

    @staticmethod
    def post(request):
        # todo make a nice tuple of data to check and then use in the grab function
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            # set image to the decoded file returned by serializer
            (_, image), name, folder = serializer.validated_data.values()
            # download the image to the local file system and return the result to the client
            result = Grab.download(name, folder, image)
            return Response({'message': result})
        else:
            return Response({'message': serializer.error_messages})
