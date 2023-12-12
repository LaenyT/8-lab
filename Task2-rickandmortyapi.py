import requests
import random
import json
from episode import Episode
from character import Character

character_id = random.randint(1, 826)
url = f'https://rickandmortyapi.com/api/character/{character_id}'
response = requests.get(url)

if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    character_data = response.json()
    print(character_data)

print("Character Keys:", character_data.keys())

with open(f'info_character_{character_id}.json', 'w') as file:
    json.dump(character_data, file)

episode_urls = character_data.get('episode', [])

with open(f'all_episodes_with_character_{character_id}.txt', 'a') as file:
    for episode_url in episode_urls:
        file.write(f"{episode_url}\n")

episode_id = 1
episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
episode_response = requests.get(episode_url)

if episode_response.status_code >= 400:
    print(f"Error: {episode_response.status_code}")
else:
    episode_data = episode_response.json()
    print("Episode Structure:", episode_data.keys())


episode_object = Episode(
    id=episode_data['id'],
    name=episode_data['name'],
    air_date=episode_data['air_date'],
    episode=episode_data['episode'],
    characters=episode_data['characters'],
    url=episode_data['url'],
    created=episode_data['created']
)

print(episode_object.get_episode_info())

episode_objects = []

for episode_id in episode_data:
    episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
    episode_response = requests.get(episode_url)

    if episode_response.status_code < 400:
        episode_data = episode_response.json()
        episode_objects.append(Episode(
            id=episode_data['id'],
            name=episode_data['name'],
            air_date=episode_data['air_date'],
            episode=episode_data['episode'],
            characters=episode_data['characters'],
            url=episode_data['url'],
            created=episode_data['created']
        ))

for episode_object in episode_objects:
    print(episode_object.get_episode_info())

character_id = 1
character_url = f'https://rickandmortyapi.com/api/character/{character_id}'
character_response = requests.get(character_url)

if character_response.status_code >= 400:
    print(f"Error: {character_response.status_code}")
else:
    character_data = character_response.json()
    print("Character Structure:", character_data.keys())

character_object = Character(
    id=character_data['id'],
    name=character_data['name'],
    status=character_data['status'],
    species=character_data['species'],
    type=character_data['type'],
    gender=character_data['gender'],
    origin=character_data['origin'],
    location=character_data['location'],
    image=character_data['image'],
    url=character_data['url'],
    created=character_data['created']
)