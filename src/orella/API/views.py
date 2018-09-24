from rest_framework.views import APIView
from rest_framework.response import Response
from .es import Grab


class WebGrab(APIView):
    """ provides back end support for webGRAB photo import app"""

    @staticmethod
    def get(request):
        """ :return: a tuple of folders from 'parent' directory"""
        return Response(Grab.get_destination_folders())

    @staticmethod
    def post(request):
        Grab.upload(request.data)
        return Response({'message': 'OK'})
