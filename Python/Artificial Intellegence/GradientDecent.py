class GradientDecent:
	def __init__(self, xy):
		self.__xy = xy
		self.__w0 = 0.1
		self.__w1 = 0.2
	def getXY(self):
		return self.__xy
	def getW0(self):
		return self.__w0
	def setW0(self,w0):
		self.__w0 = w0
	def getW1(self):
		return self.__w1
	def setW1(self,w1):
		self.__w1 = w1
	def getAlpha(self):
		return self.__a
	def batch(self):
		initialW0 = self.getW0()
		initialW1 = self.getW1()
		a = .001
		xy = self.getXY()
		n = len(xy)
		xl = [x for x,y in xy]
		yl = [y for x,y in xy]

		sum0 = 0
		sum1 = 0
		for i in xrange(n):
			sum0 += (yl[i] - self.hw(initialW0, initialW1, xl[i]))
			
			sum1 += ((yl[i] - self.hw(initialW0, initialW1, xl[i])) * xl[i])


			
		updatedW0 = initialW0 + ((a/n) * sum0)

		updatedW1 = initialW1 + ((a/n) * sum1)
		
		self.setW0(updatedW0)
		self.setW1(updatedW1)
		if abs(initialW0 - updatedW0) < 1e-7 and abs(initialW1 - updatedW1) < 1e-7:	
			return True
		else:
			return False
	def stochastic(self):
		initialW0 = self.getW0()
		initialW1 = self.getW1()
		a = .001
		xy = self.getXY()
		n = len(xy)
		xl = [x for x,y in xy]
		yl = [y for x,y in xy]
		for i in xrange(n):
			updatedW0 = initialW0 + ((a/n) * (yl[i] - self.hw(initialW0, initialW1, xl[i])))
			updatedW1 = initialW1 + ((a/n) * (yl[i] - self.hw(initialW0, initialW1, xl[i])) * xl[i])
			self.setW0(updatedW0)
			self.setW1(updatedW1)
			if abs(initialW0 - updatedW0) < 1e-7 and abs(initialW1 - updatedW1) < 1e-7:	
				return True


	def hw(self,w0,w1,x):
		return w0 + (w1 * x)
	def linearEquation(self, x):
		w0 = self.getW0()
		w1 = self.getW1()
		return w0 + w1*x
