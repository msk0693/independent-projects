class ColorFormat:
    def __init__(self):
	    self.colors = {}
	    key = 0
	    for style in range(8):
		    for fg in range(30,38):
		 		for bg in range(40,48):
		 			format = ';'.join([str(style), str(fg), str(bg)])
		 			self.colors[key] = format
		 			key +=1


    
    def printColorFormatTable(self):
        key = 0
        for style in range(8):

            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, key)
                    key += 1
                print(s1)
            print('\n')
    def printColorFormat(self,key):
        print '\x1b[%sm %s \x1b[0m' % (self.colors[key], key)

    def getColorFormat(self,key):
    	return self.colors[key]









    	    





