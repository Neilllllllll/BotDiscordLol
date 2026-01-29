from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

# Modèle représentant un compte monitoré
class AccountMonitor(Base):
    __tablename__ = "accounts"

    # On définit les colonnes avec le typage Python moderne (Mapped)
    riot_id: Mapped[str] = mapped_column(primary_key=True)
    pseudo: Mapped[str] = mapped_column(nullable=False)
    elo: Mapped[str] = mapped_column(nullable=True)
    winrate: Mapped[float] = mapped_column(default=0.0)

    def __repr__(self) -> str:
        return f"Account(id={self.riot_id}, pseudo={self.pseudo})"