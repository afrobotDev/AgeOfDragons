#Defines a new class called "Soldier"
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.health = 100 
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons 

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed 
    
    def take_damage(self, damage, multiplier):
        damage *= multiplier 
        self.health -= damage

dalinar = Soldier()
dalinar.take_damage(20,2)
print(dalinar.health)

adolin = Soldier()
adolin.take_damage(10, 3)
print(adolin.health)


soldier_one = Soldier("Legolas", 5, 1)
print(soldier_one.name)
print(soldier_one.get_speed())
print(soldier_one.armor)
print(soldier_one.num_weapons)

soldier_two = Soldier("Gimli", 6, 2)
print(soldier_two.name)
print(soldier_two.get_speed())
print(soldier_two.armor)
print(soldier_two.num_weapons)

soldier_one.take_damage(2)
print(soldier_one.health)

soldier_two = Soldier()
soldier_two.take_damage(1)
print(soldier_two.health)


# Defines a class called Archer 
class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows
    
    def take_hit(self):
        if self.health == 0:
            raise ValueError(f"{self.name} is dead")
        self.health -= 1

    def shoot(self, target):
        if self.num_arrows == 0:
            if self.health == 0:
                target.take_hit()
            else:
                raise ValueError(f"{self.name} can\'t shoot")
        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.take_hit()
        
    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")  


# Defines a class called Wall 
class Wall:
    def __init__(self, depth, height, width):
        self.armor = 10
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

    def fortify(self):
        self.armor *= 2

    def get_cost(self):
        cost_of_wall = self.armor * self.height
        return cost_of_wall
    
wall = Wall()
print(wall.get_cost())

wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)

south_wall = Wall()
south_wall.height = 20
print(south_wall.height)

wall.fortify()
print(wall.armor)


# Defines a class called Wizard
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana


# Defines a class called Dragon 
class Dragon:
  def __init__(self, element):
    self.element = element

  def get_breath_damage(self):
    if self.element == "fire":
      return 300
    if self.element == "ice":
      return 150
    return 0

def main():
    aragorn = Brawler("Aragorn", 4, 4)
    gimli = Brawler("Gimli", 2, 7)
    legolas = Brawler("Legolas", 7, 7)
    frodo = Brawler("Frodo", 3, 2) 
  
    fight(aragorn, gimli)
    fight(legolas, frodo) 
    first_dragon = Dragon("fire")
    print(
      f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
      f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )  


# Defines a class called Brawler 
class Brawler:
  def __init__(self, name, speed, strength):
    self.name = name
    self.speed = speed
    self.strength = strength
    self.power = speed * strength

def fight(attacker, defender):
  print(f"{attacker.name}: {attacker.power} power")
  print(f"{defender.name}: {defender.power} power")
  if attacker.power > defender.power:
    print(f"{attacker.name} wins!")
  elif attacker.power < defender.power:
    print(f"{defender.name} wins!")
  else:
    print("It's a tie!")
  print("--------------------------")

main()

class Human:
    def __init__(self, pos_x, pos_y, speed, stamina=10):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina

    def __sprint(self, move_method, steps=2):
        self.__raise_if_cannot_sprint()
        move_method(steps)
        self.__use_sprint_stamina()

    def sprint_right(self):
        self.__sprint(self.move_right)

    def sprint_left(self):
        self.__sprint(self.move_left)

    def sprint_up(self):
        self.__sprint(self.move_up)

    def sprint_down(self):
        self.__sprint(self.move_down)

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise ValueError("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    def move_right(self, steps=1):
        self.__pos_x += self.__speed * steps

    def move_left(self, steps=1):
        self.__pos_x -= self.__speed * steps

    def move_up(self, steps=1):
        self.__pos_y += self.__speed * steps
   
    def move_down(self, steps=1):
        self.__pos_y -= self.__speed * steps

    def get_position(self):
        return self.__pos_x, self.__pos_y


