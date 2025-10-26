from abc import ABC, abstractmethod
import copy

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def __repr__(self):
        return f"<Dog name={self.name}>"

class Training(ABC):
    @abstractmethod
    def perform_task(self):
        pass

class ServiceDog(Dog, Training):
    def __init__(self, name, age, service_type):
        super().__init__(name, age)
        self.service_type = service_type
    
    def perform_task(self):
        return f"{self.name} is performing task: {self.service_type}."
    
    def assist(self):
        return f"{self.name} is assisting with {self.service_type}."

class DogShelter:
    def __init__(self):
        self.dogs = []
        self._backup_dogs = []
        print("Shelter created.")

    def __str__(self):
        if not self.dogs:
            return "DogShelter (empty)"
        names = ', '.join([str(d) for d in self.dogs])
        return f"DogShelter (contains: {names})"
    
    def _simulate_load(self, source_str: str):
        print(f"  ...Loading from '{source_str}'...")
        if "ERROR" in source_str:
            raise IOError("File read error: data corrupted")
        
        new_dogs = []
        for item in source_str.split(','):
            name, age = item.split(':')
            new_dogs.append(Dog(name, int(age)))
        
        self.dogs = new_dogs
        print(f"  Loading successful.")

    def _simulate_save(self):
        print("  ...Attempting to save...")
        # raise IOError("Failed to save: disk full")
        print("  Save successful.")

    def __enter__(self):
        print("\n--- [ENTER] ---")
        
        self._backup_dogs = copy.deepcopy(self.dogs)
        print(f"Backup created: {self._backup_dogs}")
        
        try:
            fictional_data = "Buddy:5,Lucy:2"
            # fictional_data = "Buddy:5,ERROR:BadData"
            self._simulate_load(fictional_data)
        
        except Exception as e:
            print(f"[ENTER] Load error: {e}. Rolling back...")
            self.dogs = self._backup_dogs
            raise 
        
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("--- [EXIT] ---")
        
        if exc_type is not None:
            print(f"Error inside 'with': {exc_value}.")
            print("Save cancelled. Rolling back changes...")
            self.dogs = self._backup_dogs
            print(f"State restored: {self}")
        
        else:
            try:
                self._simulate_save()
                print(f"Final state saved successfully: {self}")
            
            except Exception as e:
                print(f"Save error: {e}.")
                print("Rolling back changes made in 'with'...")
                self.dogs = self._backup_dogs
                print(f"State restored: {self}")
        
        self._backup_dogs = []
        
        return True

print("--- 1. ServiceDog Test ---")
guard_dog = ServiceDog("Rex", 4, "Security")
print(guard_dog.bark())
print(guard_dog.perform_task())
print("-" * 20)

shelter = DogShelter()
shelter.dogs = [Dog("Sirko", 3)]
print(f"Initial state: {shelter}")

print("\n--- 2. 'with' Test (Success Case) ---")
try:
    with shelter as s:
        print("  (Inside 'with')")
        print(f"  State on entry: {s}")
        s.dogs.append(Dog("Polkan", 7))
        print(f"  State after adding: {s}")
    print(f"Final state: {shelter}")

except Exception as e:
    print(f"'with' block failed due to error: {e}")

print("\n--- 3. 'with' Test (Error Inside 'with') ---")
print(f"State before test: {shelter}")
try:
    with shelter as s:
        print("  (Inside 'with')")
        s.dogs.append(Dog("Tuz", 1))
        print(f"  State after adding: {s}")
        raise ValueError("Something went wrong!")
        # s.dogs.append(Dog("Bobik", 2))
    
except Exception as e:
    pass

print(f"Final state: {shelter}")
