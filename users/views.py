from django.shortcuts import render
from django.utils.crypto import get_random_string


# Create your views here.
print(get_random_string(32, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
