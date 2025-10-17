import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()
        print(f"✅ Connected to {self.db_name}")

    def create(self, first_name: str, last_name: str) -> None:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    def all(self) -> list:
        return Actor.objects.all()

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        Actor.objects.filter(id=pk).update(
            first_name=new_first_name, last_name=new_last_name
        )

    def delete(self, pk) -> None:
        user = Actor.objects.get(id=pk)
        user.delete()
