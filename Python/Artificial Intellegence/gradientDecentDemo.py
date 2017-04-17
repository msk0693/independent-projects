import GradientDecent

xy = [(2,5),(4,7),(6,14),(7,14),(8,17),(10,19)]

print str(xy)

batchdecent = GradientDecent.GradientDecent(xy)
stochdecent = GradientDecent.GradientDecent(xy)
maxIteration = 1000000
tests = []

print "Batch Decent\n----------------------------------"
i = 0
convergence = False
while not convergence and i < maxIteration:
	i+=1
	convergence = batchdecent.batch()
if i == maxIteration:
	print "MAX ITERATIONS REACHED"
else:
	w0, w1 = batchdecent.getW0(), batchdecent.getW1()
	print "-Weights Converged-\nIterations %d\nW0 = %f, W1 = %f " % (i, w0, w1)
	print "Linear Regression Equation: y = %f + %fx" % (w0, w1)
print"------------------------------------------------------------------------------------"
print "\nStohcastic Decent\n----------------------------------"
i = 0
convergence = False
while not convergence and i < maxIteration:
	i+=1
	convergence = stochdecent.stochastic()
if i == maxIteration:
	print "MAX ITERATIONS REACHED"
else:
	w0,w1 = stochdecent.getW0(), stochdecent.getW1()	
	print "Weights converged\nIterations %d\nW0 = %f, W1 = %f " % (i, w0, w1)
	print "Linear Regression Equation: y = %f + %fx" % (w0, w1)

print"------------------------------------------------------------------------------------"
print "\n-Enter x Values into test array, enter '0' after last entry to display results-\n"
e = 0
while True:
	e+= 1
	element = input("Enter element %d: " % (e))
	if element == 0:
		break
	else:
		tests.append(element)

print "\nTest Array:"
print str(tests)
print "\n-Batch Results-"
for i in tests:
	print "x = %d, y = %f" % (i, batchdecent.linearEquation(i))
print "-Stochastic Results"
for i in tests:
	print "x = %d, y = %f" % (i, stochdecent.linearEquation(i))

