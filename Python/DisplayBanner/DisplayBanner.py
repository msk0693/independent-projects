import os
import time
import ColorFormat

class DisplayBanner:
    
    def __init__(self):
    	self.__width = 80
    	self.__message = "enter a message in options".upper()
    	self.__c = '*'
    	self.__Colors = ColorFormat.ColorFormat()
    	self.__color = "0;0;0"
    	self.__characters = self.createCharSet(self.__c)
    	self.__speed = 0.05
    	self.activateDisplay()
    def createCharSet(self, c):
    	charSet = { 

               " " : [ "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   " ],

               "A" : [ " %s%s%s%s%s " % (c,c,c,c,c), 
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c), ], 

               "B" : [ "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s " % (c,c,c,c,c,c)],

               "C" : [ " %s%s%s%s%s%s" % (c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       " %s%s%s%s%s%s" % (c,c,c,c,c,c)],

               "D" : [ "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s " % (c,c,c,c,c,c)],

               "E" : [ "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c)],

               "F" : [ "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c)],

               "G" : [ " %s%s%s%s%s " % (c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s   %s%s%s" % (c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % (c,c,c,c,c)],

               "H" : [ "%s     %s" % (c,c), 
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c), ],        
              
               "I" : [ "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c)], 

               "J" : [ "      %s" % (c),
                       "      %s" % (c),
                       "      %s" % (c),
                       "      %s" % (c),
                       "      %s" % (c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % ( c,c,c,c,c)], 

               "K" : [ "%s     %s" % (c,c),
                       "%s    %s " % (c,c),
                       "%s   %s  " % (c,c),
                       "%s%s%s%s   " % (c,c,c,c),
                       "%s   %s  " % (c,c),
                       "%s    %s " % (c,c),
                       "%s     %s" % (c,c)],


               "L" : [ "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c)],

               "M" : [ "%s     %s" % (c,c),
                       "%s%s   %s%s" % (c,c,c,c),
                       "%s %s %s %s" % (c,c,c,c),
                       "%s  %s  %s" % (c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c)],    

               "N" : [ "%s     %s" % (c,c),
                       "%s%s    %s" % (c,c,c),
                       "%s %s   %s" % (c,c,c),
                       "%s  %s  %s" % (c,c,c),
                       "%s   %s %s" % (c,c,c),
                       "%s    %s%s" % (c,c,c),
                       "%s     %s" % (c,c)],                  
 

               "O" : [ " %s%s%s%s%s " % (c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % (c,c,c,c,c)],

               "P" : [ "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s      " % (c),
                       "%s      " % (c),
                       "%s      " % (c)],

               "Q" : [ " %s%s%s%s%s " % (c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s  %s  %s" % (c,c,c),
                       "%s   %s %s" % (c,c,c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % (c,c,c,c,c)],

               "R" : [ "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s%s%s%s%s%s " % (c,c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c)],    

               "S" : [ " %s%s%s%s%s " % (c,c,c,c,c),
                       "%s     %s" % (c,c),
                       "%s      " % (c),
                       " %s%s%s%s%s " % (c,c,c,c,c),
                       "      %s" % (c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % (c,c,c,c,c)], 

               "T" : [ "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c)],

               "U" : [ "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       " %s%s%s%s%s " % (c,c,c,c,c)],

               "V" : [ "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       " %s   %s " % (c,c),
                       "   %s   " % (c)], 

               "W" : [ "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s     %s" % (c,c),
                       "%s  %s  %s" % (c,c,c),
                       "%s %s %s %s" % (c,c,c,c),
                       "%s%s   %s%s" % (c,c,c,c),
                       "%s     %s" % (c,c)],


               "X" : [ "%s     %s" % (c,c),
                       " %s   %s " % (c,c),
                       "  %s %s  " % (c,c),
                       "   %s   " % (c),
                       "  %s %s  " % (c,c),
                       " %s   %s " % (c,c),
                       "%s     %s" % (c,c)],

               "Y" : [ "%s     %s" % (c,c),
                       " %s   %s " % (c,c),
                       "  %s %s  " % (c,c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c)],

               "Z" : [ "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c),
                       "     %s " % (c),
                       "    %s  " % (c),
                       "   %s   " % (c),
                       "  %s    " % (c),
                       " %s     " % (c),
                       "%s%s%s%s%s%s%s" % (c,c,c,c,c,c,c)], 
                
               "!" : [ "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "   %s   " % (c),
                       "       ",
                       "   %s   " % (c) ]
               
               }
        return charSet

    def getWidth(self):
    	return self.__width
    def getMessage(self):
    	return self.__message
    def setMessage(self, message):
    	self.__message = message.upper()
    def getC(self):
    	return self.__c
    def setC(self, c):
    	self.__c = c
    def getColorClass(self):
    	return self.__Colors
    def getColor(self):
    	return self.__color
    def setColor(self, color):
    	self.__color = color
    def getCharacters(self):
    	return self.__characters
    def setCharacters(self, characters):
    	self.__characters = characters
    def getSpeed(self):
    	return self.__speed
    def setSpeed(self, speed):
    	self.__speed = speed
    def activateDisplay(self):
    	width = self.getWidth()
    	message = self.getMessage()
    	formatMessage = message + (len(message) * 10 * " ")
    	color = self.getColor()
    	printMess = ["","","","","","",""]
    	characters = self.getCharacters()
    	speed = self.getSpeed()
    	print "Press control-c for options"
    	for row in range(7):
    	    for char in formatMessage:
                printMess[row] += (str(characters[char][row] + "  "))
    	offset = width

    	try:
	        while True:
	            os.system("clear")
	            for row in range(7):
	    	        print('\x1b[%sm' + " " * offset + printMess[row][max(0,offset*-1):width - offset] + '\x1b[0m') % (color)
	            offset -= 1
	            if offset <= ((len(message)+2)*6) * -1:
	               offset = width
	            time.sleep(speed)
        except KeyboardInterrupt:
		    
	        self.optionsMenu()
	        
	  
    def optionsMenu(self):
        print "\nOptions\n1: Change Message\n2: Change Drawing Character\n3: Color Options\n4: Speed Options\n5: Apply Changes\n6: Exit Program"
        option = int(input("Option: "))
        os.system("clear")    
        if option == 1:
	        newMessage = raw_input("Enter a New Message: ").upper()
	        self.setMessage(newMessage)
	        print "-New Message Set-"    	
        elif option == 2:
	        newC = raw_input("Enter a New Drawing Character: ")
	        self.setCharacters(self.createCharSet(newC))

	        print "-New Character Set-"
        elif option == 3:
		    self.colorOptions()
        elif option == 4:
		    self.speedOptions()
        elif option == 5:
            print self.getSpeed()
            self.activateDisplay()
        else :
	        print "End of Line"
	        quit()
        self.optionsMenu()
		   
    def colorOptions(self):
    	key = 0
    	Colors = self.getColorClass()
        print "\nColor Options\n1: View Colors\n2: Color Lookup\n3: Change Color\n4: Back"
        option = int(input("Option: "))
        os.system("clear")
        if option == 1:
            Colors.printColorFormatTable()
        elif option == 2:
            key = int(input("Enter a key from 0 - 511 to View the Color: "))            
            Colors.printColorFormat(key)
        elif option == 3:
            key = int(input("Enter a key from 0 - 511 to Set the Color: "))
            self.setColor(Colors.getColorFormat(key))
            print "-New Color Selected-"
            Colors.printColorFormat(key)     
        else :
            self.optionsMenu()	
        self.colorOptions()

    def speedOptions(self):
        print "\nSpeed Options\n1: Slow\n2: Default\n3: Fast\n4: Back"
        option = int(input("Option: "))
        os.system("clear")
        if option == 1:
        	self.setSpeed(0.1)
        	print self.getSpeed()
        	print "-New Speed Selected-\nSlow"
        elif option == 2:
        	self.setSpeed(0.05)
        	print "-New Speed Selected-\nDefault"
        elif option == 3:
        	self.setSpeed(0.01)
        	print "-New Speed Selected-\nFast"
        else :
        	self.optionsMenu()
        self.speedOptions()