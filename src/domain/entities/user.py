from dataclasses import dataclass
from domain.value_objects.email import Email


@dataclass
class User:
    id: int
    name: str
    email: Email

    def update_name(self, new_name: str) -> None:
        if not new_name:
            raise ValueError("Name cannot be empty")
        self.name = new_name
