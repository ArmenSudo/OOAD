class Dog:
    def __init__(self, name, age, bread):
        self._name = name
        self._age = age
        self._breed = bread

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_breed(self):
        return self._breed

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_breed(self, breed):
        self._breed = breed

    @staticmethod
    def bark():
        print("Haf-haf")

    def sit(self):
        print(self._name + " sits")

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Breed: {self._breed}")

    def sniff(self):
        print(f"{self._name} sniffs")


dog1 = Dog("Rex", 1, "Bulldog")
dog2 = Dog("Violeta", 2, "Poodle")

dog1.get_age()
dog2.get_age()
dog1.bark()
dog1.sniff()
dog1.sit()
dog2.set_name("Abudal")
dog2.display_info()


class Helicopter:
    def __init__(self, model, capacity, max_speed, full_tank):
        self._model = model
        self._capacity = capacity
        self._max_speed = max_speed
        self._full_tank = full_tank
        self._current_location = (0, 0)
        self._fuel = 0

    def fill_fuel(self, fuel):
        self._fuel = min(self._fuel + fuel, self._full_tank)

    def fly_to(self, destination):
        distance = self.calculate_distance(destination)
        if distance > self._fuel:
            print("Not enough fuel")
            return
        self._current_location = destination
        self._fuel -= distance

    def calculate_distance(self, destination):
        x1, y1 = self._current_location
        x2, y2 = destination
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def get_location(self):
        return self._current_location


helicopter = Helicopter("SA 330 (J) Puma", 6, 154, 1000)
helicopter.fill_fuel(500)
helicopter.fly_to((10, 10))
print(helicopter.get_location())


class Hospital:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._patients = {}

    def admit(self, patient, type_of_help: "Surgical(0) or therapeutic(1)"):
        if len(self._patients) >= self._capacity:
            print("Hospital is full")
            return
        self._patients[patient] = type_of_help

    def discharge(self, patient):
        if patient not in self._patients:
            print("Patient not found")
            return
        self._patients.pop(patient)

    def get_patients(self):
        return self._patients


hospital = Hospital("Astxik", 500)
hospital.admit("John Smith", 0)
hospital.admit("Jim Cery", 1)
print(hospital.get_patients())
hospital.discharge("John Smith")
print(hospital.get_patients())
