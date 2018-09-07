# understand the problem
  # State a solution to the problem in english

# What is the end goal?
  # Return a list containing integers from num down to 0
# What are the inputs?
  # An integer
# What is the output?
  # A list
# Can we make any assumptions about the inputs?
  # Input will definitely be positive
  # Input will definitely be an integer


# pseudo-code
# create a function called countdown that accepts num
  # def countdown(num):
# create a list
  # set variable my_list to store an empty list
  # my_list = []
# while(num >= 0)
# Take the num, add it to the list
  # append num to my_list
  # my_list.append(num)
# subtract one from the num
  # num = num - 1
  # OR num -= 1
# after loop, return my_list

# know what a given set of inputs should output
# Run through it on a t-diagram
# How do we test our work in code?
# after those 2 steps, we can run the code

def countdown(num):
  my_list = []
  while(num >= 0):
    my_list.append(num)
    num -= 1
  return my_list

x = countdown(3)
# print(x)


# input is one list with at least 2 values
# output is printing of value one and returning of value 2

# create a function called print_and_return that accepts one list with at least 2 values
# def print_and_return(arr):
  # print the first one
  # access first value
    # arr[0]
  # print(arr[0])
  # return second value
  # access second value
    # arr[1]
    # return arr[1]

def print_and_return(arr):
  print(arr[0])
  return arr[1]

# How do we test?
  # run the function
  # function block should print first value
  # print returned value
    # store and print
    # print function invocation
# print(print_and_return([5,10]))


users_list = [
  {
    'name': "Wes",
    'favorite_food': "Sushi",
    'favorite_artist': "Vanilla Ice"
  },
  {
    'name': "Scott",
    'favorite_food': "Tacos",
    'favorite_artist': "Enya"
  },
  {
    'name': "Jason",
    'favorite_food': "Souls",
    'favorite_artist': "Limp Bizkit"
  }
]

# for index in range(0, 10):
#   print(index)

# for user_dict in users_list:
#   for key in user_dict.keys():
#     print(user_dict[key])

words_list = ['thing', 'other', 'bad word', 'hi']

class Person:
  def __init__(self, name, favorite_artist, favorite_food):
    self.name = name
    self.favorite_artist = favorite_artist
    self.favorite_food = favorite_food
    self.health = 100
    self.speed = 20

  def introduce(self):
    print("Hi my name is " + self.name + " I'm feeling okay with " + str(self.health) + " health")
    return self

  def workout(self):
    self.speed += 5
    return self

  def brag(self):
    print("My speed is " + str(self.speed))
    return self

  def eat(self, amount):
    self.health += amount
    return self

class Ninja(Person):
  def __init__(self, name, favorite_artist, favorite_food):
    super().__init__(name, favorite_artist, favorite_food)
    self.health = 120

person1 = Ninja('Wes', 'Enya', 'Sushi')
person2 = Person('Jason', "Tool", "Tacos")
person1.introduce() #"Hi my name is {name}"
person2.introduce() #"Hi my name is {name}"
person1.brag().workout().workout().workout().workout().workout().introduce().brag().eat(100).introduce()
print(person1.speed)