from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    
    @staticmethod
    def from_user(user):
        return User(user.id, user.name)
       
