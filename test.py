from classes import System, Body, Planet, Star, Moon

solar_system = System.create()
sun = Star("Sun", 1.989*(10**30), "G")
earth = Planet("Earth", 5.972*(10**24), 24, 365)
luna = Moon("Luna", 7.342*(10**22), 27, earth)

solar_system.add(sun)
solar_system.add(earth)
solar_system.add(luna)
solar_system.add(luna)

alpha_centauri = System.create()
alpha_centauri_a = Star("Alpha Centauri A", 2.188*(10**30), "G")
alpha_centauri_b = Star("Alpha Centauri B", 1.804*(10**30), "K")
alpha_centauri_c = Star("Alpha Centauri C", 2.446*(10**29), "G")

alpha_centauri.add(alpha_centauri_a)
alpha_centauri.add(alpha_centauri_b)
alpha_centauri.add(alpha_centauri_c)
alpha_centauri.add(alpha_centauri_c)

print()
print("Bodies in the solar system:")
print(solar_system)
print("Total mass:")
print(solar_system.total_mass())

print()
print("Bodies in the alpha centauri system:")
print(alpha_centauri)
print("Total mass:")
print(alpha_centauri.total_mass())

for s in [solar_system, alpha_centauri]:
    for c in [Body, Planet, Star, Moon]:
        print()
        print("Find all objects of type {} in the solar system (currently):".format(c.__name__))
        for b in c.all(s):
            print(b)

print()
print("Total galactic mass:")
print(System.mass_of_all_systems())
