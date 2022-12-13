import requests


class SuperHeroManager:

    def __init__(self):
        self.url = 'https://akabab.github.io/superhero-api/api/'

    def get_all_heroes(self):
        response = requests.get(self.url + 'all.json')
        return response.json()

    def choose_the_smartest(self, names):
        json_data = self.get_all_heroes()
        hero_int = {}
        for hero in json_data:
            if hero['name'] in names:
                hero_int[hero['name']] = hero['powerstats']['intelligence']
        heros_int = dict(sorted(hero_int.items(), key=lambda item: item[1]))
        return list(heros_int.keys())[0]


manager = SuperHeroManager()
print(manager.choose_the_smartest(['Captain America', 'Hulk', 'Thanos']))

