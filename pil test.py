import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import requests

new_im = Image.new('RGB', (8000,  8000))

image1 = Image.open(requests.get('https://i.scdn.co/image/ab67616d0000b273f48c78b65a59d62bfe4046ab', stream=True).raw)

new_im.paste(image1,(0,0,460,460))

image2 = Image.open(requests.get('https://i.scdn.co/image/ab67616d0000b273f48c78b65a59d62bfe4046ab', stream=True).raw)

#new_im.paste(image2,(460,0))

new_im.save('test.jpg')
new_im.show()