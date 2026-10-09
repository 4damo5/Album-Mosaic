# Album-Mosaic

Builds a collage of album covers from a Spotify playlist using Spotipy and Pillow. Three layouts: square grid, 16:9 phone wallpaper, and 19.5:9 iPhone wallpaper.

<img src="/mosaic.jpg" width="500" />

## Usage
1. Create an app on the Spotify for Developers dashboard and set `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`.
2. Set `PLAYLIST_ID` in `album_collage.py`.
3. Uncomment the layout you want at the bottom of the file.
4. `pip install spotipy pillow requests` then `python3 album_collage.py`

The playlist needs at least as many unique albums as tiles in the mosaic.
