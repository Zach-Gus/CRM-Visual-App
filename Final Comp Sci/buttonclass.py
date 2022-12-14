# buttonClass.py
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""
    
    
    def __init__(self, win, center, width, height, color,label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() ##this line was not there in class, what does it do?

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True
    
    ##check 3.  complete the deactivate() method
        
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False 
        

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        ##your code here
        return (p.getX() >= self.xmin and p.getX()
                <= self.xmax and p.getY() >= self.ymin and p.getY() <= self.ymax
                and self.active) 
            
            
        

 
