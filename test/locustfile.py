from locust import HttpUser, TaskSet, task

class PokedexLoadTest(TaskSet):
    @task(1)
    def load_homepage(self):
        """Test de charge pour la page d'accueil."""
        self.client.get("/")

    @task(2)
    def load_pokemon_data(self):
        """Test de charge pour le chargement des données Pokémon."""
        for i in range(1, 151):  # Tester les 150 premiers Pokémon
            self.client.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

    @task(1)
    def test_static_files(self):
        """Test de charge pour les fichiers statiques (CSS, JS)."""
        self.client.get("/style.css")
        self.client.get("/script.js")

class WebsiteUser(HttpUser):
    tasks = [PokedexLoadTest]
    min_wait = 1000  # Temps d'attente min entre deux requêtes (ms)
    max_wait = 5000  # Temps d'attente max entre deux requêtes (ms)
