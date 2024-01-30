from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def firebase_configs(request):
    if request.method == "GET":
        firebase_config = {
            "apiKey": "AIzaSyAMzmOZ79qPniWx399VJvfPmXmKIECgEJY",
            "authDomain": "django-firebase-4d325.firebaseapp.com",
            "databaseURL": "https://django-firebase-4d325-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId": "django-firebase-4d325",
            "storageBucket": "django-firebase-4d325.appspot.com",
            "messagingSenderId": "185167762255",
            "appId": "1:185167762255:web:274990549d5de2698f2b3a",
            "measurementId": "G-ZMYJKFW50E",
        }
        return JsonResponse({"firebase_config": firebase_config})
    return JsonResponse({"Error": "Method not allowed!"})


urlpatterns = [
    path("r/admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("users/", include("users.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("firebase/configuration/file/", firebase_configs),
]
