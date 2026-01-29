# Class qui permettra d'interagir avec l'API riot
class RiotService:
    def __init__(self, api_key, bdd_service):
        self.api_key = api_key
        self.bdd = bdd_service

    def fetch_player_data(self, player_id):
        # Logique pour interagir avec l'API Riot et récupérer les données du joueur
        pass

    def update_player_stats(self, player_id):
        # Logique pour mettre à jour les statistiques du joueur dans la BDD
        player_data = self.fetch_player_data(player_id)
        if player_data:
            self.bdd.update_player_record(player_id, player_data)