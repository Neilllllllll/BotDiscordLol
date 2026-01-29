from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models import AccountMonitor
import time

class BddService:
    def __init__(self, host, database, user, password, port):
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        # 1. Création du moteur de base de données
        self.engine = create_engine(db_url)
        
        # 2. Création d'une "usine" à sessions
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # 3. Attente de la BDD et création des tables
        self._init_db()

    def _init_db(self):
        retries = 5
        while retries > 0:
            try:
                # Crée les tables définies dans "Base" si elles n'existent pas
                AccountMonitor.metadata.create_all(self.engine)
                print("Tables synchronisées avec succès !")
                break
            except Exception as e:
                print(f"Erreur connexion ({retries} essais restants): {e}")
                retries -= 1
                time.sleep(2)

    def save_account(self, account_data: AccountMonitor):
        """Ajoute ou met à jour un compte."""
        with self.SessionLocal() as session:
            with session.begin(): # Gère automatiquement le commit/rollback
                # merge vérifie si l'ID existe : il update si oui, insert si non
                session.merge(account_data)

    def get_all_accounts(self):
        """Récupère tous les comptes."""
        with self.SessionLocal() as session:
            # Nouveau style SQLAlchemy 2.0 (select)
            stmt = select(AccountMonitor)
            return session.scalars(stmt).all()