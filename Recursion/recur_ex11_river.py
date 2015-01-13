def river_crossing_this(m1 = 3, c1 = 3, m2 = 0, c2 = 0):
	print "%d missionaries and %d cannibals on this bank" % (m1, c1)
	print "%d missionaries and %d cannibals on other bank" % (m2, c2)
	if m1 < c1 and c1 >= 2:
		print "2 cannibals cross river on boat to other bank\n"
		river_crossing_other(m2, c2 + 2, m1, c1 - 2)
	elif m1 >= c1 + 2 and m1 >= 2:
		print "2 missionaries cross river on boat to other bank\n"
		river_crossing_other(m2 + 2, c2, m1 - 2, c1)
	else:
		print "1 missionary and 1 cannibal cross river on boat to other bank\n"
		river_crossing_other(m2 + 1, c2 + 1, m1 - 1, c1 - 1)
		
def river_crossing_other(m2, c2, m1, c1):
	print "%d missionaries and %d cannibals on this bank" % (m1, c1)
	print "%d missionaries and %d cannibals on other bank" % (m2, c2)
	if m1 == 0 and c1 == 0:
		print "Completed!"
	elif m2 > c2:
		print "1 missionary cross river on boat to this bank\n"
		river_crossing_this(m1 + 1, c1, m2 - 1, c2)
	else:
		print "1 cannibal cross river on boat to this bank\n"
		river_crossing_this(m1, c1 + 1, m2, c2 - 1)
		
river_crossing_this(m1 = 5, c1 = 5)