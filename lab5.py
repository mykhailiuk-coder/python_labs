from abc import ABC, abstractmethod
import copy


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")


class Training(ABC):

    @abstractmethod
    def perform_task(self):
        pass


class ServiceDog(Dog, Training):

    def __init__(self, name, age, service_type):
        super().__init__(name, age)
        self.service_type = service_type

    def perform_task(self):
        print(f"{self.name} is performing: {self.service_type}.")


class DogShelter:
    def __init__(self, dogs, name, location):
        self.dogs = dogs
        self._backup_dogs = []
        self.name = name
        self.location = location

    def _simulate_load(self):
        print("Trying to load new data...")

        return [Dog("Buddy", 5), Dog("Lucy", 2)]

    def __enter__(self):

        self._backup_dogs = copy.deepcopy(self.dogs)
        print(f"Backup was made: {self._backup_dogs}")

        try:

            new_data = self._simulate_load()
            self.dogs = new_data
            print(f"Successful load. Current state: {self.dogs}")

        except Exception as e:

            print(f"Load error: {e}. Returning to a backup...")
            self.dogs = self._backup_dogs

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:

            print(f"'with' block error: {exc_value}. Backup...")
            self.dogs = self._backup_dogs

        else:

            print("Exiting successful load.")

        self._backup_dogs = []
        return True


my_service_dog = ServiceDog("Buddy", 5, "Guide")
my_dog = Dog("Jacky", 8)
my_shelter = DogShelter([my_service_dog, my_dog], "Favpaws", "Arkansas")

my_service_dog.get_info()
my_dog.get_info()
my_service_dog.bark()
my_dog.bark()
my_service_dog.perform_task()

print("==========================")
my_shelter.dogs[0].name = "ChangedName"
print(f"Before 'with' block: {[dog.name for dog in my_shelter.dogs]}")
try:
    with my_shelter as shelter:
        shelter.dogs[1].name = "NewName"
        print(f"In 'with' block: {[dog.name for dog in shelter.dogs]}")
        raise ValueError("Something went wrong")
except ValueError as e:
    pass

new_shelter = DogShelter(Dog("newbuddy", 4), Dog("newjacky", 8), "Washington")
try:
    with new_shelter as shelter:
        print(f"In 'with' block: {[dog.name for dog in shelter.dogs]}")
except Exception as e:
    pass
