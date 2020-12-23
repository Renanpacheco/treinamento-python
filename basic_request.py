import requests
'''
def print_data_zip(cep):
    response=requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    data_zip=response.json()
    #return data_zip


def print_data_pokemon(pokemon):
    response=requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    print(response.status_code)
    #print(response.text)
    data_poke=response.json()
    print(data_poke['sprites']['front_shiny'])
    #return data_poke
'''
def request_sites(url):
    response=requests.get(url)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    #cep=input('please enter a zip code(without -): ')
    #pokemon=input('pokemon: ')
    #print_data_zip(cep)
    #print_data_pokemon(pokemon)
    url='https://www.google.com/'
    request_sites(url)







#print(response.text)
#print(response.json())
#print(type(response.json()))
#cep=response.json()
#print(cep['logradouro'])
#print(cep['complemento'])