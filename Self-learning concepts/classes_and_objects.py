class Enemy: #by class we mean, hey python, we gonna make a class. Its a common practice of programmers to use first upper case letter to make a class. It helps to differeniae a class from veriable or functions.
    life = 3
    def attack(selff):
        print("Ouuuch, I'm attacked")
        selff.life -= 1

    def checklife(selfff):
        if selfff.life <= 0:
            print("Agh, Im fucked up")
        else:
            print("I'm {} life left".format(selfff.life))


    def print(self):
        print(self)
##
##enemy1_object = Enemy() #objects are actually a copy of the class
##enemy2_object = Enemy() #we can make as many ibjects as we want and they are independednt of each other.
##
##enemy1_object.attack() #
##enemy1_object.attack() # by running these finctions, the variable in the class(life) will be updated and saved independent.
##enemy1_object.attack() #
##
##enemy1_object.checklife()
##enemy2_object.checklife()
##

#https://www.youtube.com/watch?v=POQIIKb1BZA


'''
        self.pt1 = Point(min(pt1.x, pt2.x), min(pt1.y, pt2.y)) ##
        self.pt2 = Point(max(pt2.x,pt1.x), max(pt2.y, pt1.y)) ##
'''
