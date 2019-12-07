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
    i=0
    while i < 50:
        ponto = win.getMouse()
        if ponto.getX() > 1100 and ponto.getX() < 1200 and ponto.getY() > 650 and ponto.getY() < 700:
            m.turn()
            m.show_world()
            i+=1
            t = Text(Point(1175,50), i)
            t.draw(win)