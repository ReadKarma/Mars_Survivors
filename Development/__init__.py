
from State import State

import tkinter

class Game(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.pack()

        self.turn = 0
        self.game_state = State(100,0,4.0,100,20,0.35,0.1,0.2,10)

        self.ui_frame = tkinter.Frame(self)
        self.ui_frame.pack(side="right")

        self.next_turn_button = tkinter.Button(self.ui_frame, text = "Next Turn", command = self.next_turn)
        self.next_turn_button.pack()
    
        self.turn_frame = tkinter.Frame(self.ui_frame)
        self.turn_frame.pack()
        self.turn_display = tkinter.Label(self.turn_frame, text = "Turn: ")
        self.turn_display.pack(side="left")
        self.turn_display_no = tkinter.Label(self.turn_frame, text = 0)
        self.turn_display_no.pack(side="right")

        self.people_displays = tkinter.Frame(self)
        self.people_displays.pack()

        self.farmer_display = PeopleDisplay(self.people_displays, "Farmers")
        self.cleaner_display = PeopleDisplay(self.people_displays, "Cleaners")
        self.collector_display = PeopleDisplay(self.people_displays, "Collectors")
        self.maint_display = PeopleDisplay(self.people_displays, "Maintenance")
    
        self.render_state()

    def next_turn(self):
        self.turn += 1
        self.game_state.turn()
        #simular o turno
        self.render_state()

    def render_state(self):
        self.turn_display_no["text"] = self.turn
        self.farmer_display.update_list([person for person in self.game_state.people if person.get_work() == 'farm'])
        self.cleaner_display.update_list([person for person in self.game_state.people if person.get_work() == 'cleans'])
        self.collector_display.update_list([person for person in self.game_state.people if person.get_work() == 'collects'])
        self.maint_display.update_list([person for person in self.game_state.people if person.get_work() == 'maint'])
    

class PeopleDisplay(tkinter.Frame):
    def __init__(self, master, list_name):
        super().__init__(master)
        self.pack(side="left")
        
        self.name_label = tkinter.Label(self, text = list_name)
        self.name_label.pack()
        
        self.list_frame = tkinter.Listbox(self)
        self.list_frame.pack()

    def update_list(self, people_list):
        self.list_frame.delete(0, tkinter.END)
        for person in people_list:
            self.list_frame.insert(tkinter.END, person.get_name())



root = tkinter.Tk()
win = Game(root)
win.mainloop()


i=0
while i < 500:
    ponto = win.getMouse()
    if ponto.getX() > 1100 and ponto.getX() < 1200 and ponto.getY() > 650 and ponto.getY() < 700:
        m.turn()
        m.show_world()
        i+=1
        t = Text(Point(1175,50), i)
        t.draw(win)
    elif ponto.getX() > 1100 and ponto.getX() < 1200 and ponto.getY() > 120 and ponto.getY() < 170:
        i = 500
    for yass in range(m.get_number_people()):
        guys_place = m.people[yass].get_place()
        if ponto.getX() > guys_place.getX() and ponto.getX() < (guys_place.getX() + 20) and ponto.getY() > guys_place.getY() and ponto.getY() < (guys_place.getY() + 20):
            ponto = win.getMouse()
            if ponto.getX() > 70 and ponto.getX() < 290 and ponto.getY() > 120 and ponto.getY() < 700:
                m.people[i].update_work('farm')
            if ponto.getX() > 320 and ponto.getX() < 540 and ponto.getY() > 120 and ponto.getY() < 700:
                m.people[i].update_work('cleans')
            if m.getX() > 570 and ponto.getX() < 790 and ponto.getY() > 120 and ponto.getY() < 700:
                m.people[i].update_work('collects')
            if ponto.getX() > 820 and ponto.getX() < 1040 and ponto.getY() > 120 and ponto.getY() < 700:
                m.people[i].update_work('maint')