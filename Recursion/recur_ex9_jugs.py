def jugs(vlarge = 4, vsmall = 3, target = 2, vleft = 0):
	if vleft > vsmall:
		print "Pour %dL from large jug into small jug" % vsmall
		
		vleft -= vsmall
	
	else:
		if vleft > 0:
			print "Pour %dL from large jug into small jug" % vleft
	
		print "Fill large jug"
	
		vpour = vsmall - vleft
		print "Pour %dL from large jug into small jug" % vpour
		
		vleft = vlarge - vpour
		
	print "Pour away the full small jug"
	print "%dL left in large jug" % vleft
		
	if vleft == target:
		print "Completed"
	else:
		print
		jugs(vlarge, vsmall, target, vleft)
		
jugs(12, 7, 8)