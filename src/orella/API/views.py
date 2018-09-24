from rest_framework.views import APIView
from rest_framework.response import Response
from .es import Grab


class WebGrab(APIView):
    """ provides back end support for webGRAB photo import app"""

    @staticmethod
    def get(request, format=None):
        """ :return: a tuple of folders from 'parent' directory"""
        return Response(Grab.get_destination_folders())
