import math

print("Pokemon Distance Calculator")
print("---------------------------------")

pokemon1_name= input("Enter the name of the first Pokemon: ")
pokemon1_xcoord= float(input("Enter x coordinate of first pokemon: "))
pokemon1_ycoord= float(input("Enter y coordinate of first pokemon: "))

pokemon2_name= input("Enter the name of the second Pokemon: ")
pokemon2_xcoord= float(input("Enter x coordinate of second pokemon: "))
pokemon2_ycoord= float(input("Enter y coordinate of second pokemon: "))

pokemon_distance= ((pokemon2_xcoord-pokemon1_xcoord)**2)+((pokemon2_ycoord-pokemon1_ycoord)**2)

distance= math.sqrt(pokemon_distance)
print("The distance between",pokemon1_name,"and",pokemon2_name,"is",format(distance, ".2f"),"inches.")
print("---------------------------------")