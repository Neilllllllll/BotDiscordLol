from app.services.riot_service import RiotService
from app.services import BddService
from app.config.config import DISCORD_TOKEN, CHANNEL_ID, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT, RIOT_API_KEY
    
if __name__ == "__main__":
    bdd = BddService(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
    # riot_service = RiotService(api_key=RIOT_API_KEY, bdd_service=bdd)