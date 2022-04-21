from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test the API View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as its methods (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        # must return a Response object.
        # The Response should contain a list or a dictionary.
        # It converts it to JSON
        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview
        })
