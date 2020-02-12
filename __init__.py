from graphics import *
from State import State

#def main():

#    c = Circle(Point(50,50), 10)
#    c.draw(win)
#    win.getMouse() # Pause to view result
#    win.close()    # Close window when done

if __name__ == "__main__":
    win = GraphWin("Mars Survivors", 1350, 735)
    m = State(100,0,4.0,100,20,0.35,0.1,0.2,10,win)
    m.show_world()
    t = Text(Point(1175,50), 0)
    t.draw(win)
    i=0
    while i < 500:
        ponto = win.getMouse()
        if ponto.getX() > 1100 and ponto.getX() < 1300 and ponto.getY() > 650 and ponto.getY() < 700:
            m.turn()
            m.show_world()
            i+=1
            t = Text(Point(1175,50), i)
            t.draw(win)
        elif ponto.getX() > 1100 and ponto.getX() < 1300 and ponto.getY() > 120 and ponto.getY() < 170:
            i = 500
        for yass in range(m.get_number_people()):
            guys_place = m.people[yass].get_place()
#            dist=guys_place-ponto
#            norm_dist=Math.sqrt(dist.getX()^2+dist.getY()^2)
            if ponto.getX() > guys_place.getX() and ponto.getX() < guys_place.getX() + 10 and ponto.getY() > guys_place.getY() and ponto.getY() < guys_place.getY() + 10:
                ponto = win.getMouse()
                if ponto.getX() > 70 and ponto.getX() < 290 and ponto.getY() > 120 and ponto.getY() < 700:
                    m.people[i].update_work('farm')
                if ponto.getX() > 320 and ponto.getX() < 540 and ponto.getY() > 120 and ponto.getY() < 700:
                    m.people[i].update_work('cleans')
                if ponto.getX() > 570 and ponto.getX() < 790 and ponto.getY() > 120 and ponto.getY() < 700:
                    m.people[i].update_work('collects')
                if ponto.getX() > 820 and ponto.getX() < 1040 and ponto.getY() > 120 and ponto.getY() < 700:
                    m.people[i].update_work('maint')