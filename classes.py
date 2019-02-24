class System:

    # class variable
    systems = []

    # class methods
    @classmethod
    def create(cls):
        new_system = System()
        cls.systems.append(new_system)
        return new_system

    @classmethod
    def mass_of_all_systems(cls):
        galactic_mass = 0
        for system in cls.systems:
            galactic_mass += system.total_mass()
        return galactic_mass

    # instance methods
    def __init__(self):
        # instance variables
        self.bodies = []

    def __str__(self):
        s = ""
        for body in self.bodies:
            i = self.bodies.index(body)
            if i == (len(self.bodies) - 1):
                s += "* {}".format(body.name)
            else:
                s += "* {}\n".format(body.name)
        return s

    def add(self, body):
        if body in self.bodies:
            print("{} has already been added!".format(body.name))
        else:
            self.bodies.append(body)

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body.mass
        return total


class Body:
    # class method
    @classmethod
    def all(cls, system):
        bodies_found = []
        for b in system.bodies:
            if isinstance(b, cls):
                bodies_found.append(b)
        return bodies_found

    # instance method
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __str__(self):
        return "* {}".format(self.name)


class Planet(Body):
    # instance method
    def __init__(self, name, mass, day, year):
        # call parent's (superclasse's) init method first
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):
    # instance method
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type


class Moon(Body):
    # instance method
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet
