from rest_framework.views import APIView
from .serializers import PostSerializer, ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Application
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PostViewset(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,resuest):
        posts = Post.objects.filter(occupied=0)
        if not posts.exists():
            return Response({"message": "No posts found."}, status=404)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_id = request.data.get("post_id")
        file = request.data.get("file")
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        email_address = user.email
        print("first_name", first_name)
        print("last_name", last_name)
        print("email_address", email_address)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=404)
        application_exists = Application.objects.filter(user=user, post=post).exists()
        if application_exists:
            return Response({'message': 'You already applied for this position'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplicationSerializer(
            data={'post': post.id, 'user': user.id, 'first_name': first_name, 'last_name': last_name, 'email_address': email_address, 'file': file}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'Application saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"massages": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




