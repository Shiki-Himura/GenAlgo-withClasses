#imports
import Evolution

# main program which will call all the functions
evo = Evolution.Generation()
evo.generate_origin()

while not evo.is_Target:
    evo.generate_heritage()
