class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.url = url
        self.created = created

    def get_character_info(self):
        return f"{self.name} (ID: {self.id}, Status: {self.status}, Species: {self.species})"