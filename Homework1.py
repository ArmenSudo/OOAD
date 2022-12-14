# Make frog, sun, grass, air, tree classes
import time
import os



class Air:
    def __init__(self):
        self._state = True

    def change_state(self, flag):
        self._state = flag

    def state(self):
        return self._state


class Sun:
    def __init__(self):
        print("Sun Activate")
        self.is_day_time = True

    def change_time(self, flag, tree_instance, air_instance):
        self.is_day_time = flag

        print("sun on" if self.is_day_time else "sun off")
        if not flag:
            tree_instance.off_make_air(air_instance)
        else:
            tree_instance.make_air(self, air_instance)

    def state(self):
        return self.is_day_time


class Tree:
    def __init__(self, sun_instance: Sun, air_instance: Air):
        if sun_instance.is_day_time:
            print("Tree Make air")
            print("Air is turn-on")
            self._make_air_var = True
            air_instance.change_state(self._make_air_var)
        else:
            print("Turn-on sun tree doesn't make air")
            self._make_air_var = False
            air_instance.change_state(self._make_air_var)

    def make_air(self, sun_instance: Sun, air_instance: Air):
        if sun_instance.is_day_time:
            print("Tree Make air")
            print("Air is turn-on")
            self._make_air_var = True
            air_instance.change_state(self._make_air_var)
        else:
            print("Turn-on sun tree doesn't make air")
            self._make_air_var = False
            air_instance.change_state(self._make_air_var)

    def off_make_air(self, air_instance: Air):
        self._make_air_var = False
        air_instance.change_state(self._make_air_var)
        print("Tree doesnt Make air")

    def state(self):
        return self.make_air


class Grass:
    def __init__(self):
        self.count = 100

    def be_eaten(self):
        if self.count == 0:
            print("Grass end")
        else:
            print("frog eating")
            time.sleep(2)
            self.count -= 10
            print("the frog finished eating 10 grass")

    def add_grass(self, sun_instance: Sun):
        if sun_instance.is_day_time:
            self.count += 10
        else:
            print("Sun is turn-off")

    def grass_count(self):
        return self.count


class Frog:
    def __init__(self):
        self._eating_var = False
        self._breathe_var = False
        self._awake_var = False

    def eats_grass(self, grass_instance: Grass):
        if not self._awake_var:
            print("Frog is sleeping!")
        elif self._eating_var:
            print("Frog is already eating")
        elif not self._breathe_var:
            print("It sleeping")
        else:
            self._eating_var = True
            grass_instance.be_eaten()
            self._eating_var = False

    def _breathe(self, air_instance: Air):
        if air_instance.state():
            self._breathe_var = True
        else:
            print("Not air")

    def wake_up(self, sun_instance: Sun, air_instance: Air):
        if sun_instance.is_day_time:
            self._breathe(air_instance)
            self._awake_var = True
            print("Frog is wake-up")
        else:
            print("Sun is turn-off")

    def sleep(self):
        print("The frog fell asleep")
        self._breathe_var = False
        self._awake_var = False


class Controller:
    def __init__(self):
        self.sun_obj = Sun()
        self.air_obj = Air()
        self.tree_obj = Tree(self.sun_obj, self.air_obj)
        self.gras_obj = Grass()
        self.frog = None

    def turn_on_sun(self):
        self.sun_obj.change_time(True, self.tree_obj, self.air_obj)

    def turn_of_sun(self):
        self.sun_obj.change_time(False, self.tree_obj, self.air_obj)

    def tree_make_air(self):
        self.tree_obj.make_air(self.sun_obj, self.air_obj)

    def tree_off_make_air(self):
        self.tree_obj.off_make_air(self.air_obj)

    @staticmethod
    def sleep(frog_instance: Frog):
        frog_instance.sleep()

    def wake_up(self, frog_instance: Frog):
        frog_instance.wake_up(self.sun_obj, self.air_obj)

    def eat_grass(self, frog_instance: Frog):
        if self.air_obj.state():
            frog_instance.eats_grass(self.gras_obj)
        else:
            print("Air is off")


os.system('clear')
frog1 = Frog()
controller_obj = Controller()
time.sleep(3)
os.system('clear')

for x in range(3):
    controller_obj.wake_up(frog1)
    time.sleep(1)


controller_obj.turn_on_sun()
time.sleep(1)

controller_obj.turn_of_sun()
print("Eat")
controller_obj.eat_grass(frog1)

controller_obj.turn_on_sun()
print("Eat")
controller_obj.eat_grass(frog1)