from data import locations

direction = {
	'west': (-1, 0),
	'east': (1, 0),
	'north': (0, -1),
	'south': (0, 1),
}

position = (0,0)

while True
	locations= locatiomns[position]
	print 'you are at the %s' % location

	valid_directions = {}
	for k, v in directions.interitems():
		possible_position = (position[0] + v[0], posistion[1] + v[1])
		possible_locations = locations.get(possoble_postion)
		if possible_location:
			print 'to the %s is a %s' % (k, possible_location)
			valid_directions[k] = posible_posistion

		direction = raw_input('which direction do you want go?\n')
		postion = valid directions[direction]