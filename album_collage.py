import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import requests
import os
import random

#INTIIAL VARS TO CALL API
PLAYLIST_ID = 'YOUR-PLAYLIST-ID'

#scope for api
scope = 'playlist-modify-public'

#MAKE SURE YOU MAKE THE ENVIRONMENT VARS
spotifyObject = sp.Spotify(auth_manager=SpotifyOAuth(scope=scope)) 

print('obj made')

#FIRST PLAYLIST
TRACKS = spotifyObject.playlist_items(PLAYLIST_ID, offset=0)

#playlist song total
playlist_size = TRACKS['total']

print('tracks acquired')

#LIST OF ALBUM COVERS
album_list = []

#OFFSET TRACKER
offset_var = 0

#Loops over all playlist songs and reacts to the offset change

#basically splits the offset into units of 100 so depending on 
#how many hundreds the total playlist has will determine how many loops it goes through
while offset_var // 100 <= TRACKS['total'] // 100:
    print(f'processing playlist block {offset_var // 100 + 1}...')
    #loops over the 100 songs queued in
    for song in range(len(TRACKS['items'])):
        #put the album cover in the list
        try:
            if TRACKS['items'][song]['track']['album']['images'][0]['url'] not in album_list:
                album_list.append(TRACKS['items'][song]['track']['album']['images'][0]['url']) #SIZE OF EACH COVER: 640x640
                #print(song + 1 + offset_var , TRACKS['items'][song]['track']['album']['images'][0]['url'])
        
        #if the song is invalid dont factor it in
        except:
            pass
    
    #queues into the next 100 songs
    offset_var += 100

    #changes tracks to the new queue
    TRACKS = spotifyObject.playlist_items(PLAYLIST_ID, offset=offset_var)

#it is done
print('playlist analyzed')

#function for printing square album mosiac
def square_mosaic(m_size):
    #create the folder for the covers if not already made
    if not os.path.isdir('./Square_Covers'):
        print('making folder...')
        os.mkdir('./Square_Covers')

    #clear the folder
    for file in os.listdir('./Square_Covers'):
        os.remove('./Square_Covers/' + file)

    #creates array of random album covers in playlist
    print('generating list of album covers...')
    album_num_list = set()
    for cover in range(m_size ** 2):
        num = random.randint(0, len(album_list))
        while num in album_num_list:
            num = random.randint(0, len(album_list))
        album_num_list.add(num)
    album_num_list = list(album_num_list)

    #dictionary of links to index them because idk
    album_images = {}

    #saves each album cover while also putting each into the album dictionary
    print('saving covers...')
    for cover in range(m_size ** 2):
        album_images[cover] = Image.open(requests.get(album_list[album_num_list[cover]], stream = True).raw)
        album_images[cover].save('./Square_Covers/' + str(cover) +'.jpg')

    #final output image
    new_im = Image.new('RGB', (640 * m_size, 640 * m_size))

    #puts all the covers together
    print('compiling final image...')
    for y in range(m_size): 
        print('row' + str(y + 1) + 'complete')
        for x in range(m_size):
            #album cover coords
            ys = y * 640
            xs = x * 640

            #this algorithm (x + y + y * (size - 1)) was figured out w/ 'figuring out grid algo.png'
            curr_image = Image.open('./Square_Covers/' + str(x + y + y * (m_size - 1)) + '.jpg')
            new_im.paste(curr_image,(xs, ys))

    #saves the final image and opens it
    print('saving and opening image...')
    new_im.save('Square Album Mosaic.jpg')
    new_im.show()

#function for printing phone album mosiac
def phone_mosaic(m_size):
    #create the folder for the covers if not already made
    if not os.path.isdir('./Phone_Covers'):
        print('making folder...')
        os.mkdir('./Phone_Covers')

    #clear the folder
    for file in os.listdir('./Phone_Covers'):
        os.remove('./Phone_Covers/'+file)

    #creates array of random album covers in playlist
    print('generating list of album covers...')
    album_num_list = set()
    for cover in range(m_size ** 2 * 144):
        num = random.randint(0, len(album_list))
        while num in album_num_list:
            num = random.randint(0, len(album_list))
        album_num_list.add(num)
    album_num_list = list(album_num_list)
    
    #dictionary of links to index them because idk
    album_images = {}

    #saves each album cover while also putting each into the album dictionary
    print('saving covers...')
    for cover in range(m_size ** 2 * 144):
        album_images[cover] = Image.open(requests.get(album_list[album_num_list[cover]], stream = True).raw)
        album_images[cover].save('./Phone_Covers/' + str(cover) + '.jpg')

    #final output image
    new_im = Image.new('RGB', (640 * m_size * 9, 640 * m_size * 16))

    #puts all the covers together
    print('compiling final image...')
    for y in range(m_size * 16):
        print('row ' + str(y + 1) + ' complete')
        for x in range(m_size * 9):
            #album cover coords
            ys = y * 640
            xs = x * 640

            #this algorithm (x + y + y * size * 8) was figured out w/ 'figuring out grid algo for phone.png'
            curr_image = Image.open('./Phone_Covers/' + str(x + y + y * (m_size) * 8) + '.jpg')
            new_im.paste(curr_image, (xs, ys))

    #saves the final image and opens it
    print('saving and opening image...')
    new_im.save('Phone Album Mosaic.jpg')
    new_im.show()

#function for printing iphone album mosiac
def iphone_mosaic(m_size):
    #create the folder for the covers if not already made
    if not os.path.isdir('./Phone_Covers'):
        print('making folder...')
        os.mkdir('./Phone_Covers')

    #clear the folder
    for file in os.listdir('./Phone_Covers'):
        os.remove('./Phone_Covers/'+file)

    #creates array of random album covers in playlist
    print('generating list of album covers...')
    album_num_list = set()
    for cover in range(m_size ** 2 * 19 * 9):
        num = random.randint(0, len(album_list))
        while num in album_num_list:
            num = random.randint(0, len(album_list))
        album_num_list.add(num)
    album_num_list = list(album_num_list)
    
    #dictionary of links to index them because idk
    album_images = {}

    #saves each album cover while also putting each into the album dictionary
    print('saving covers...')
    for cover in range(m_size ** 2 * 19 * 9):
        album_images[cover] = Image.open(requests.get(album_list[album_num_list[cover]], stream = True).raw)
        album_images[cover].save('./Phone_Covers/' + str(cover) + '.jpg')

    #final output image
    new_im = Image.new('RGB', (640 * m_size * 9, 640 * m_size * 19))

    #puts all the covers together
    print('compiling final image...')
    for y in range(m_size * 19):
        print('row ' + str(y + 1) + ' complete')
        for x in range(m_size * 9):
            #album cover coords
            ys = y * 640
            xs = x * 640

            #this algorithm (x + y + y * size * 8) was figured out w/ 'figuring out grid algo for phone.png'
            curr_image = Image.open('./Phone_Covers/' + str(x + y + y * (m_size) * 8) + '.jpg')
            new_im.paste(curr_image, (xs, ys))

    #saves the final image and opens it
    print('saving and opening image...')
    new_im.save('Phone Album Mosaic.jpg')
    new_im.show()



#make grid of album covers in a square** done
#take input for the square mosaic
# square_size = int(input(f'input num from 2 to {int((playlist_size ** .5))}\n'))

# square_mosaic(square_size)

#make a phone background of album covers**
#take input for the phone mosaic
# phone_size = int(input(f'input num from 1 to {playlist_size // 144}\n'))

# phone_mosaic(phone_size)

#make an iphone x+ background of album covers**
#take input for the phone mosaic
phone_size = int(input(f'input num from 1 to {playlist_size // 16 // 9}\n'))

iphone_mosaic(phone_size)
