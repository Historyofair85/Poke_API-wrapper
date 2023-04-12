!pip install requests
import requests

base_url = "https://pokeapi.co/api/v2/"
api_method = "pokemon/"

pokemon = input('Enter the name of your Pokemon: ').lower()
api_url = f"{base_url}{api_method}{pokemon}"
print(api_url)

poke_response = requests.get(api_url)
poke_data = poke_response.json()

name = poke_data['name']
order = poke_data['order']
poke_type = poke_data['types'][0]['type']['name']
weight = poke_data['weight']
height = poke_data['height']

class PokemonInfo:
    
    def __init__(self):
        pass
    
    def get_stat(self):
        print(f"POKEDEX")
        print(f"NAME: {name.upper()}")       
        print(f"ORDER NO. #0{order}")
        print(f"POKEMON TYPE: {poke_type.title()} ")
        print(f"HEIGHT: {height}")
        print(f"WEIGHT: {weight}")
    

pokemon1 = PokemonInfo()      
pokemon1.get_stat()