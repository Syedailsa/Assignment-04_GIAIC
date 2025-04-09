#user earth weight
weight_on_earth = float(input("Enter your weight on Earth: "))  # Get user input

#planet user selected
planet = input("Enter a planet: ").lower()

all_planets = [
{"mercury": 37.6 },

{"venus": 88.9 },

{"mars": 37.8 },

{"jupiter": 236.0},

{"saturn": 108.1},

{"uranus": 81.5},

{"neptune": 114.0}]

#find the planet
planet_percentage = None
for p in all_planets:
    for name, gravity in p.items():
        if planet == name.lower():
            planet_percentage = gravity


def Weight_func():
    planet_gravity = planet_percentage / 100  # Convert percentage to decimal
    weight_on_planet = weight_on_earth * planet_gravity  

    # Round to 2 decimal places
    rounded_weight = round(weight_on_planet, 2)  

    print(f"Your weight on {planet} is: {rounded_weight}")

Weight_func()