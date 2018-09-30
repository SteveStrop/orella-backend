import base64
from rest_framework import serializers
from django.utils.six import string_types
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        decoded_file = ''
        # Check if this is a base64 string
        if isinstance(data, string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                data = data.split(';base64,')[1]

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)

            except TypeError:
                self.fail('invalid_image')
            data = ContentFile(decoded_file, name='_.jpg')
        # call to_internal_value and return the decoded version of the file
        return super(Base64ImageField, self).to_internal_value(data), decoded_file


class ImageSerializer(serializers.Serializer):
    image = Base64ImageField(max_length=None, use_url=True)
    name = serializers.CharField(max_length=7)
    folder = serializers.CharField(max_length=200)
