from datetime import time
from discord.ext import tasks
import discord

class DiscordService:
    def __init__(self, token, bdd_service, channel_id):
        self.token = token  
        self.bdd = bdd_service
        self.channel_id = channel_id
        
        # Configuration des intents (Permissions nécessaires)
        intents = discord.Intents.default()
        intents.message_content = True  # Important pour lire les messages
        
        self.client = discord.Client(intents=intents)

        # Enregistrement des événements
        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f'Connecté en tant que {self.client.user} !')

        if not self.daily_report.is_running():
            self.daily_report.start()

    async def on_message(self, message):
        # Ne pas répondre à soi-même
        if message.author == self.client.user:
            return

        # Commande d'exemple : !citation
        if message.content.startswith('!test'):
            # 1. Lire la BDD
            #texte = self.bdd.get_random_citation()
            # 2. Envoyer le message
            await self.send_message("Tu as lancé la commande !test")
            
    # Définition de la tâche récursive
    @tasks.loop(seconds=3) 
    async def daily_report(self):
        print(f"Il est 20h, récupération des données...")
        
        # Récupérer les données via ton service BDD
        # data = self.bdd.get_ranking() # On réutilise ton exemple précédent

        # --- CORRECTION 2 : Pour passer à 20h plus tard ---
        # Il suffira de remplacer le décorateur par :
        # @tasks.loop(time=time(hour=20, minute=0))

        await self.send_message("ceci est un message récursif !")

    async def send_message(self, message_text):
        """Envoie un message sur un canal donné."""
        try:
            channel = self.client.get_channel(self.channel_id)
            if channel:
                await channel.send(message_text)
            else:   
                print(f"Canal avec l'ID {self.channel_id} introuvable.")
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")

    def run(self):
        self.client.run(self.token)