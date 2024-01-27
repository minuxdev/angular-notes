import pyrebase


firebase_config = {

  "apiKey": "AIzaSyAMzmOZ79qPniWx399VJvfPmXmKIECgEJY",

  "authDomain": "django-firebase-4d325.firebaseapp.com",

  "databaseURL": "https://django-firebase-4d325-default-rtdb.asia-southeast1.firebasedatabase.app",

  "projectId": "django-firebase-4d325",

  "storageBucket": "django-firebase-4d325.appspot.com",

  "messagingSenderId": "185167762255",

  "appId": "1:185167762255:web:274990549d5de2698f2b3a",

  "measurementId": "G-ZMYJKFW50E"

}


firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()

def image_uploader(image):
    url = storage.child(f'images/posts/{image}').put(image)
    return url['name']

def get_image_url(image):
    url = storage.child(f'{image}').get_url(image)
    return url
