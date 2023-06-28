class Materia:
    def __init__(self, id, title): #el self era para autoreferenciarse
        self.id = id
        self.title = title
        
    def __str__(self):
        return f'id = {self.id} título = {self.title}'