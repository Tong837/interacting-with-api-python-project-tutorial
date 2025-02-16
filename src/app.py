
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sns

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

id_artista="4AOiNpcmfXTiWDB3uFszgn"

results = spotify.artist_top_tracks(id_artista)

data = []


for track in results['tracks'][:10]:
    data.append({
         "Cancion": track['name'],
         "Popularidad": track['popularity'],
         "Duración": track['duration_ms']
    })


df = pd.DataFrame(data)
df_sorted = df.sort_values(by="Popularidad", ascending=True)
print(df)

#CREAR SCATTER PLOT, GUARDAR EN VAR SCATTER PLOT
# RELLENA : scatter_plot = linea que genera la grafica
plt.scatter.get_figure(8,5)
plt.scatter(df["duracion_ms"], df["popularidad"], color="orange", alpha=0.6)

#CACMBIAR NOMBRE A LAS COLMUMNAS POR NAME CORRESPONDIENTE Y NO COMO 0,1,2




