##########          SCOPE          ##########

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope and Global Scope - Differences between those 2 is where you define. If a variable is declared just inside the function, it is a local variable, acessible only there #

# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")