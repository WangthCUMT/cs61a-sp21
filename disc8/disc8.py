import math
pi = math.pi

class Shape:
    """All geometric shapes will inherit from this Shape class."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))

class Circle(Shape):
    """A circle is characterized by its radii"""
    def __init__(self, name, radius):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        "*** YOUR CODE HERE ***"
        return 2 * pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        "*** YOUR CODE HERE ***"
        return pi * (self.radius) ** 2

class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more inconvenient."""
    def __init__(self, name, num_sides, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        "*** YOUR CODE HERE ***"
        return self.num_sides * self.side_length
class Square(RegPolygon):
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name, 4, side_length)

    def area(self):
        """Returns the area of a square (squared side length)"""
        "*** YOUR CODE HERE ***"
        return self.side_length ** 2

class Triangle(RegPolygon):
    """An equilateral triangle"""
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name,3, side_length)

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = math.sqrt(3)/4
        "*** YOUR CODE HERE ***"
        return constant * self.side_length ** 2



class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(f'{self.name} says meow!')
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.lives > 0:
            self.lives -= 1
        else:
            self.is_alive = False
            print('This cat has no more lives to lose.')
    def revive(self):
        """Revives a cat from the dead. The cat should now have
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.__init__(self.name,self.owner)  # __init__方法也可以调用
        else:
            print('This cat still has lives to lose.')

class NoisyCat(Cat):
    """A Cat that repeats things twice."""

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()