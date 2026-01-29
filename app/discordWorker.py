from app.services import DiscordService
from app.services import BddService
from app.config.config import DISCORD_TOKEN, CHANNEL_ID, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

if __name__ == "__main__":
    # Initialisation des services de la BDD et du bot Discord
    bdd = BddService(host="db", database="botdb", user="user", password="password", port=5432)
    discord_bot = DiscordService(DISCORD_TOKEN, bdd, CHANNEL_ID)
    
    # Démarrage du bot
    try:
        print("Démarrage du bot Discord...")
        discord_bot.run()
    except KeyboardInterrupt:
        bdd.close()
    print("Bot arrêté.")
