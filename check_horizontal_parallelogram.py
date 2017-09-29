def get_line_function_solved_x(slope, point):
	# define a function that takes in y and returns x
	def line_function_solved_x(y):
		# return the x value when y is plugged in
		return float(y - point[1])/float(slope) + point[0]
	# return the function
	return line_function_solved_x

def get_slope(p1, p2):
	# basic slope calculation
	return (float(p1[1] - p2[1])/float(p1[0] - p2[0]))

def check_horizontal_parallelogram(point_coords, par_coords):
	# sort the coords of the parallelogram first by y and then by x
	par_coords.sort(key=lambda x: (x[1], x[0]))

	# unpack the coords of the parallelogram
	bl = par_coords[0]
	br = par_coords[1]
	ul = par_coords[2]
	ur = par_coords[3]

	#unpack the point coords
	xp = point_coords[0]
	yp = point_coords[1]

	# check if the y value of the point given is in between the y values of the parallelogram
	if (yp < bl[1] or yp > ul[1]):
		# if so, the point is either above or below the parallelogram
		return False

	# check if the parallelogram is a rectangle
	if (bl[0] == ul[0]):
		# if so, do a simple comparison against the sides
		if (xp < bl[0] or xp > br[0]):
			# if so, point is either to the right or left of the parallelogram
			return False
		else:
			# if not, point is inside the rectangle!
			return True
	# if we get there, we know the parallelogram is not a rectangle

	#get the slope of the left and right sides
	slope = get_slope(ul, bl)

	#get the line function for the left side by passing in the bottom left point
	left_line_function_solved_x = get_line_function_solved_x(slope, bl)
	#get the line function for the right side by passing in the bottom right point
	right_line_function_solved_x = get_line_function_solved_x(slope, br)

	#get the x value for the point on the left side that has the same y value as the given point
	xl = left_line_function_solved_x(yp)
	#get the x value for the point on the right side that has the same y value as the given point
	xr = right_line_function_solved_x(yp)

	# check if the x value of the given point is in between xl and xr
	if (xp >= xl and xp <= xr):
		# if so, the point is in the parallelogram!
		return True
	else:
		# otherwise, the point is to the left or right of the parallelogram
		return False


