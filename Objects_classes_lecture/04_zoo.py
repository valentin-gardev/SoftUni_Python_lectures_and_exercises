class Zoo:
    __animals = 0
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []




    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species_in_zoo):
        if species_in_zoo == 'mammal':
            animals = ', '.join(self.mammals)
            return f"{species_in_zoo.capitalize() + 's'} in {self.name_zoo}: {animals}\nTotal animals: {Zoo.__animals}"
        elif species_in_zoo == 'fish':
            animals = ', '.join(self.fishes)
            return f"{species_in_zoo.capitalize() + 'es'} in {self.name_zoo}: {animals}\nTotal animals: {Zoo.__animals}"
        elif species_in_zoo == 'bird':
            animals = ', '.join(self.birds)
            return f"{species_in_zoo.capitalize() + 's'} in {self.name_zoo}: {animals}\nTotal animals: {Zoo.__animals}"



name_zoo = input()
zoo = Zoo(name_zoo)
count_animals = int(input())
for _ in range(count_animals):
    animal_info = input().split()
    species,  name = animal_info

    zoo.add_animal(species, name)
species_in_zoo = input()
print(zoo.get_info(species_in_zoo))

