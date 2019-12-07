'''
Created on 11/10/2019

@author: Miguel
'''

import random

class Person:

    def __init__(self, happiness, prob_farm, prob_cleans, prob_maint, name):
        self.happiness = happiness
        self.base_happiness = happiness

        r = random.Random().random()
        if r < prob_farm:
            self.work_obj = 'farm'
        elif r < (prob_farm + prob_cleans):
            self.work_obj = 'cleans'
        elif r < (prob_farm + prob_cleans + prob_maint):
            self.work_obj = 'maint'
        else:
            self.work_obj = 'collects'
        self.work = self.work_obj
        self.name = name
        

    def update_happiness(self, cleans):
        if self.work == self.work_obj:
            self.happiness = cleans/5
        else:
            self.happiness = (cleans/5)-10

    def update_work(self, new_work):
        self.work = new_work

    def get_happiness(self):
        return self.happiness

    def get_cleans(self):
        return self.work == 'cleans'

    def get_food(self):
        return self.work == 'farm'

    def get_money(self):
        return self.work == 'maint'

    def get_materials(self):
        return self.work == 'collects'
    
    def get_work(self):
        return self.work
    
    def get_name(self):
        return self.name

    def update_place(self, location):
        self.place = location