from models import Base, Employee, Post  # les autres sont chargés transitvement
from models.base import init_db, get_db_session

if __name__ == "__main__":
    init_db(delete=False)
    with get_db_session() as session:
        pass

