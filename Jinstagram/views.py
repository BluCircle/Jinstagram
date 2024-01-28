from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("the get is called.")
        return render(request, "Jinstagram/main.html")
    
    # def post(self, request):
    #     print("the post is called.")
    #     return render(request, "Jinstagram/main.html")
    