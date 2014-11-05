#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="magenta")
player = drawpad.create_oval(240,240,260,260, fill="blue")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "pink")
		self.button1.grid(row=0,column=0)
		
		self.button5 = Button(self.myContainer1)
		self.button5.configure(text="Left", background= "pink")
		self.button5.grid(row=0,column=1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "pink")
		self.button2.grid(row=0,column=2)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Down", background= "pink")
		self.button4.grid(row=1,column=1)
				
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button5.bind("<Button-1>", self.button5Click)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button4.bind("<Button-1>", self.button4Click)
		

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		drawpad.move(player, 0, -20)


		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)

                # Do your if statement - remember to return True if successful!
                
        def button2Click(self, event):   
		drawpad.move(player, 20, 0)
                global oval
		global drawpad
	
	def button5Click(self, event):   
		drawpad.move(player, -20, 0)
                global oval
		global drawpad
	
	def button4Click(self, event):   
		drawpad.move(player, 0, 20)
                global oval
		global drawpad	
		
	
direction = 1
def animate():
    global direction
    global target
    targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
    if targetx2 > drawpad.winfo_width():
            direction = - 1
    elif targetx1 < 0: 
            direction = 1
    drawpad.move(target,direction,0)
    drawpad.after(1,animate)
animate()	    
		
myapp = MyApp(root)

root.mainloop()