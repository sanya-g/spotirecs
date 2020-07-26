import requests

# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQAct1yTXzJoNISfYGPe5zGfZu4SGq35C_Dn1CYentl1gCJGO0PPd4-TqVgGyaa3YMBRwNM-lTmIW1kFqRgFKhSydiE7u3M9CaG3OYfYivlh6M0cDen8gDg8ZvOdq1rG0pIhYQAONpkS1oOO2emN-cBmP6crUqK4_EjKTWQi_BbwRRRoSc8OEK6VGYBxAib_Jd3hd48UJVA"
user_id = "milliehuangg" 

# OUR FILTERS
#limit=20
limit = input("how many songs would you like in your playlist?\n")
market="US"
#seed_genres="contemporary r&b"
seed_genres = input("what genre are you vibing with right now? answer in the following format: contemporary r&b , indie , etc.\n")
target_danceability=float(input("how dance-able do you want your playlist to be? answer from 0.1-0.9 with .9 being the most danceable\n"))
#target_danceability=0.9
uris = [] 
seed_artists = '2h93pZq0e7k5yf4dywlkpM'
seed_tracks='6JdS5rJvJaRA7B1tcm7kxZ'

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
#query += f'&seed_tracks={seed_tracks}'
#query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('\nRecommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

    
# CREATE A NEW PLAYLIST

import requests
import json 

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "suggested "+seed_genres+" beats <3",
          "description": "program by millz, sani g, and trish at hobby hacks <3",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']
#print(response.status_code)

# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

#print(response.status_code)
print(f'Your playlist is ready at {url}\n')

