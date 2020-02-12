'''
Created on 11/10/2019

@author: Miguel
'''
from Person import Person
from graphics import *

class State:

    def __init__(self, cleans, materials, happiness, food, money, prob_farm, prob_cleans, prob_maint, number_people, win):
        self.prob_farm = prob_farm
        self.prob_cleans = prob_cleans
        self.prob_maint = prob_maint
        self.food = food
        self.cleans = cleans
        self.happiness = happiness
        self.materials = materials
        self.money = money
        self.number_people = number_people
        self.win = win
        self.people =list()
        for i in range(number_people):
            a = Person(happiness, prob_farm, prob_cleans, prob_maint, str(i+1))
            self.people.append(a) 

    def new_work(self, new_work, name):
        i=0
        while i < self.number_people:
            if self.people[i].get_name() == name:
                self.people[i].update_work(new_work)

    def show_list(self, list_name, people2_list, x0, y):
        t = Text(Point(x0 + 60,y), list_name)
        t.draw(self.win)
        y += 35
        x = x0
        line_count = 0
        for dude in people2_list:
            t = Text(Point(x,y), dude.get_name())
            t.draw(self.win)
            dude.update_place(Point(x,y))
            x += 40
            line_count += 1
            if line_count == 5:
                y += 20
                line_count = 0
                x = x0


    def show_values(self):
        x = 60
        for i in range(5):
            x += 100
            if i == 4:
                t = Text(Point(x,50), self.happiness)
                t.draw(self.win)
            elif i == 3:
                t = Text(Point(x,50), self.materials)
                t.draw(self.win)
            elif i == 2:
                t = Text(Point(x,50), self.food)
                t.draw(self.win)
            elif i == 1:
                t = Text(Point(x,50), self.cleans)
                t.draw(self.win)
            else:
                t = Text(Point(x,50), self.money)
                t.draw(self.win)

    def turn(self):
        r = len(self.people)
        i=0
        while i<r:
            self.people[i].update_happiness(self.cleans)
            i+=1
        i=0
        s=0
        while i<r:
            s+=self.people[i].get_happiness()
            i+=1
        self.happiness=r/s
        if self.cleans>=90:
            if self.happiness>=10:
                self.happiness=self.happiness*1.2
            else:
                self.happiness+=2
        self.happiness+=(self.money*0.1)
        i=0
        nr_farmers=0
        while i<r:
            if self.people[i].get_work() == 'farm':
                nr_farmers+=1
            i+=1
        self.food+=nr_farmers
        if self.happiness<0:
            self.food = self.food/2
        nr_people = int(self.food/10)
        if nr_people<r:
            death = r-nr_people
            for i in range(death):
                self.people.pop(0)
        elif nr_people>r:
            life = nr_people - r
            j=int(self.people[r-1].get_name())
            for i in range(life):
                a = Person(self.happiness, self.prob_farm, self.prob_cleans, self.prob_maint, str(i+j+1))
                self.people.append(a)
        if self.number_people > 1000:
            self.number_people=1000
        if self.number_people<0:
            self.number_people=0

    def clear(self):
        for item in self.win.items[:]:
            item.undraw()
        self.win.update()

    def get_number_people (self):
        return self.number_people

    def show_world(self):
        self.clear()
        self.show_list('Farmers:', [person for person in self.people if person.get_work() == 'farm'], 100, 150)
        self.show_list('Cleaners:', [person for person in self.people if person.get_work() == 'cleans'], 350, 150)
        self.show_list('Collectors:', [person for person in self.people if person.get_work() == 'collects'], 600, 150)
        self.show_list('Workers:', [person for person in self.people if person.get_work() == 'maint'], 850, 150)
        self.show_values()
        r = Rectangle(Point(1100, 650),Point(1300, 700))
        r.draw(self.win)
        t = Text(Point(1150,675),'Next Turn')
        t.draw(self.win)
        t = Text(Point(1150,50), 'Turn: ')
        t.draw(self.win)
        r = Rectangle(Point(1100, 120),Point(1300, 170))
        r.draw(self.win)
        for i in range(4):
            r = Rectangle(Point(70 + 250*i, 120),Point(290 + 250*i, 700))
            r.draw(self.win)
        t = Text(Point(1150,145), 'Surrender')
        t.draw(self.win) 