import matplotlib.pyplot as plt
import random
from font import *
from check_horizontal_parallelogram import *
import math

## CONTROLS ##
print_graph = True
save_as = 'figure_h.eps'
print_box_outlines = False

# the number of nodes
num_nodes = 30000

# height and width 	
height = 3000
width = 3000

# the distance from the side when nodes reach uniform density
side_cutoff = 300

# closeness metric
closeness = 70

# number of edges
number_of_edges = 27000

# add weight of text edges
weight = 11

# formatting
possible_node_colors = ["black"]
possible_edge_colors = ["red"]
box_edge_color = "green"

# pixel length
pixel_length = 50

# set up the heigh and width of a character
char_height = 5 * pixel_length
char_width = char_height

# set up length of margin
margin_length = 30

def plot_and_print_graph(nodes, edges, boxes):
	# assign each node a number in a dictionary
	node_to_number = {}

	for i, node in enumerate(nodes):
		node_to_number[str(node)] = i

	# go through each edge and create a tuple that has
	# the number of node 1, the number of node 2, and 1/distance
	# between them
	interactions = []

	for edge in edges:
		dist = math.hypot(edge[1][0] - edge[0][0], edge[1][1] - edge[0][1])
		p1 = node_to_number[str(edge[0])]
		p2 = node_to_number[str(edge[1])]
		interactions.append((p1, p2, 1/float(dist)))

	# open up for_dsd file
	with open(save_as[:-4] + "_for_dsd.tab", "w") as f:
		#print out interactions
		for i in interactions:
			f.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n")


	# create the xs and ys of the nodes
	xs = [n[0] for n in nodes]
	ys = [n[1] for n in nodes]

	cm = plt.get_cmap("RdYlGn")
	col = [cm(float(i)/(30)) for i in xrange(30)]


	# add the nodes
	plt.scatter(xs, ys, edgecolors='none', c=random.choice(possible_node_colors), s=3)

	# get length of all of the edges
	len_edges = len(edges)

	# loop through the edges
	for i, edge in enumerate(edges):
		statement = "Now adding " + str(i) + " out of " + str(len_edges)
		statement += " Percentage is " + str((float(i)/float(len_edges)) * 100) + "%"
		print statement
		# plot the xs and ys
		plt.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], c=random.choice(possible_edge_colors), linewidth=.2)

	# check if should print outlines of boxes
	if print_box_outlines:
		# loop through each box
		for group_of_boxes in boxes:
			for box in group_of_boxes:
				# plot the bottom
				xs = [box[0][0], box[1][0]]
				ys = [box[0][1], box[1][1]]
				plt.plot(xs, ys, c=box_edge_color)

				# plot the left side
				xs = [box[0][0], box[2][0]]
				ys = [box[0][1], box[2][1]]
				plt.plot(xs, ys, c=box_edge_color)

				# plot the right side
				xs = [box[1][0], box[3][0]]
				ys = [box[1][1], box[3][1]]
				plt.plot(xs, ys, c=box_edge_color)

				# plot the top side
				xs = [box[2][0], box[3][0]]
				ys = [box[2][1], box[3][1]]
				plt.plot(xs, ys, c=box_edge_color)

	plt.savefig(save_as, format='eps', dpi=1000)

	# print the plot
	plt.show()

def get_random_nodes(nodes):
	# define list of possible y values
	pos_y = []

	# loop through the first half of y values
	for i in range(height/2):
		# add i i times to pos_y
		for x in range(i):
			# append i to pos_y
			pos_y.append(i)

	# loop through the second half of y values doing the same but opposite
	for i in range(height/2, height):
		# add i height - i times
		for x in range(height - i):
			# append i to pos_y
			pos_y.append(i)

	# define list of possible x values
	pos_x = []

	# loop through the values up to side_cutoff
	for i in range(side_cutoff):
		# add i i times to pos_x
		for x in range(i):
			# append i to pos_x
			pos_x.append(i)

	# loop through the values from one side_cutoff to the other
	for i in range(side_cutoff, (width - side_cutoff)):
		# add side_cutoff amount of i
		for x in range(side_cutoff):
			# append i to pos_x
			pos_x.append(i)

	# loop through the values after the final side_cutoff
	for i in range(width - side_cutoff, width):
		# add i width - i times
		for x in range(width - i):
			# append i to pos_y
			pos_x.append(i)



	# loop through the number of nodes
	for i in range (num_nodes):
		x = random.choice(pos_x)
		y = random.choice(pos_y)
		new_node = (x, y)
		# append random integers based on the size of the graph
		nodes.append(new_node)

def get_line():
	# get line from user
	line = raw_input("Text: ")
	# return line as list of characters
	return list(line)

def get_edges_and_boxes(nodes, line):

	# Gets a list of groups of boxes based on the lines
	#
	# A box is defined as 4 values: the bottom left node, the bottom right node,
	#	the top left node, and the top right node and
	#		box type: [bottom_left, bottom_right, top_left, top_right]
	#
	# A group of boxes is a list of boxes associated with a specific letter in the final picture
	#		group type: [box1, box2, box3, ...]
	#
	# A list of a group of boxes contains all the information in the picture

	groups_of_boxes = get_groups_of_boxes(line)

	# get all of the combination of nodes, returns a list of pairs of nodes
	# does not include two nodes being the same
	all_combo_nodes = get_combo_nodes_near_to_eachother(nodes)

	# returns a list of pairs of nodes where those pairs that define an edge within
	# a group of boxes is listed weight more times than other pairs
	weighted_list_of_node_pairs = get_weighted_list_of_node_pairs(groups_of_boxes, all_combo_nodes)

	# randomly select number_of_edges number from the weighted list
	edges = randomly_select_edges(weighted_list_of_node_pairs)

	return (edges, groups_of_boxes)

def get_groups_of_boxes(line):
	# get a list of tuples of characters with their bottom left coordinate
	chars_with_bottom_left = get_chars_with_bottom_left(line)

	# get groups of boxes from the chars with bottom left
	groups_of_boxes = [get_group_of_boxes(char_with_bottom_left) for char_with_bottom_left in chars_with_bottom_left]

	return groups_of_boxes

	# return [[{'bl': (50, 50), 'h': 50, 'w': 50},
	# 		 {'bl': (100, 50), 'h': 50, 'w': 50},
	# 		 {'bl': (100, 100), 'h': 50, 'w': 50}]]

def get_chars_with_bottom_left(line):

	# initialize list to hold chars with bottom left
	chars_with_bottom_left = []

	# get the bottom left coordinate of the first character
	first_char_bottom_left = get_first_char_bottom_left(line)

	# add the first_char_bottom left to list
	chars_with_bottom_left.append((line[0], first_char_bottom_left))

	# loop through the rest of the characters after the first
	for i, char in enumerate(line[1:]):
		# calculate the x coordinate for char
		x = first_char_bottom_left[0] + (i + 1) * (char_width + margin_length)
		# calculate the y coordiante for char
		y = first_char_bottom_left[1]
		# append the character and the coordinates to chars_with_bottom_left
		chars_with_bottom_left.append((char, (x, y)))

	return chars_with_bottom_left

def get_first_char_bottom_left(line):

	# get the number of characters in the line
	num_characters = len(line)

	# get the total width of the line as will be plotted on the graph
	line_width = (num_characters * char_width) + ((num_characters - 1) * margin_length)

	# get the x coordinate of the bottom left position of the first character
	x = (width - line_width)/2

	# get the y coordinate of the bottom left position of the first character
	y = (height - char_height)/2
	return (x, y)

def get_group_of_boxes(char_with_bottom_left):

	# unpack char_with_bottom_left
	char = char_with_bottom_left[0]
	cbl_x = char_with_bottom_left[1][0]
	cbl_y = char_with_bottom_left[1][1]

	# get the local coordinates for boxes based on the character
	# type: [[coord1, coord2, ...], ...]
	local_coords = get_local_coords_for_char_boxes(char)

	# map get box from local coords onto the list of local coords, passing in 
	# the coordinates of the bottom left of the character
	group_of_boxes = [get_box_from_local_coords(lc, cbl_x, cbl_y) for lc in local_coords]

	return group_of_boxes

def get_local_coords_for_char_boxes(char):
	#return what ever is the value when using
	#char as a key in the imported font dictionary
	return font[char]

def get_box_from_local_coords(local_coords, cbl_x, cbl_y):
	# sort the local coords by the y coordinates and then the x coordinates
	local_coords.sort(key=lambda p: p[1])
	local_coords.sort(key=lambda p: p[0])

	# map get_local_to_canvas_coord over local coords, passing in cbl_x and cbl_y
	# this gives us the values on the canvas for the box, not the relative values
	new_box = [get_local_to_canvas_coord(c, cbl_x, cbl_y) for c in local_coords]

	#return new_box
	return new_box

def get_local_to_canvas_coord(c, cbl_x, cbl_y):
	# get the x value by multiplying pixel length 
	x = cbl_x + (pixel_length * c[0])
	# get the y value by multiplying pixel length 
	y = cbl_y + (pixel_length * c[1])
	# return the coordinate as (x, y)
	return (x, y)

def get_combo_nodes_near_to_eachother(nodes):
	# initialize list of nodes_close_by
	nodes_close_by = []

	# loop through the nodes twice
	for n1 in nodes:
		for n2 in nodes:
			# check if the nodes are the same
			if n1[0] == n2[0] and n1[1] == n2[1]:
				# if so, continue
				continue
			else:
				# check if the nodes are close by
				if (abs(n1[0] - n2[0]) < closeness and abs(n1[1] - n2[1]) < closeness):
					# if so, add the pair of nodes to nodes_close_by
					nodes_close_by.append((n1, n2))

	return nodes_close_by

def get_all_combo_nodes(nodes):
	# initiailze list of all_combo_nodes
	all_combo_nodes = []

	# loop through the nodes twice
	for n1 in nodes:
		for n2 in nodes:
			# check if the nodes are the same
			if n1[0] == n2[0] and n1[1] == n2[1]:
				# if so, continue
				continue
			else:
				# add the pair of nodes to all_combo_nodes
				all_combo_nodes.append((n1, n2))

	return all_combo_nodes

def get_weighted_list_of_node_pairs(groups_of_boxes, all_combo_nodes):
	# initialize the weighted list
	weighted_list = []

	# get length of all_combo_nodes
	length_all_combo_nodes = len(all_combo_nodes)

	# loop through each pair of nodes
	for i, pair in enumerate(all_combo_nodes):
		statement = "Now caluclating " + str(i) + " out of " + str(length_all_combo_nodes)
		statement += " Percentage is " + str((float(i)/float(length_all_combo_nodes)) * 100) + "%"
		print statement
		# check if that pair is in a group of boxes
		if check_pair_nodes_in_groups_of_boxes(pair, groups_of_boxes):
			# if so, loop weight number of times (to append the pair that many times)
			for i in range(0, weight):
				# append to the weighted list the pair
				weighted_list.append(pair)
		#if not, append to the weighted list only once
		else:
			weighted_list.append(pair)	

	return weighted_list

def check_pair_nodes_in_groups_of_boxes(pair_nodes, groups_of_boxes):
	# loop through the groups of boxes
	for group_box in groups_of_boxes:
		# check the pair of nodes in that group box, if true return true
		if check_pair_nodes_in_group_box(pair_nodes, group_box):
			return True
	# if gotten here, return false
	return False

def check_pair_nodes_in_group_box(pair_nodes, group_box):
	# loop through each box in group box
	for box in group_box:
		# check if the first node is in the box
		if check_node_in_box(pair_nodes[0], box):
			#if so, check the second node
			if check_node_in_box(pair_nodes[1], box):
				#if so, return True
				return True

	# if we have gotten here, the nodes are not in the same box, return false
	return False

def check_node_in_box(node, box):
	# call function imported from check_horizontal_parallelogram
	return check_horizontal_parallelogram(node, box)	

def randomly_select_edges(weighted_list_of_node_pairs):
	# initialize edges set
	edges = set()

	# shuffle the node pairs
	random.shuffle(weighted_list_of_node_pairs)
	
	### Return the first number_of_edges unique node pairs
	# initialize index to 0
	i = 0

	# loop the length of the set is equal to number of edges
	while(len(edges) != number_of_edges):
		# add the node pair at i to the set
		edges.add(weighted_list_of_node_pairs[i])
		# increment i
		i += 1

	return list(edges)

if __name__ == "__main__":
	#list of nodes as pairs of x, y
	nodes = []

	# fill nodes
	get_random_nodes(nodes)

	# get the lines from the user
	line = get_line()

	# get the edges and boxes! this is where the magic happens
	edges_and_boxes = get_edges_and_boxes(nodes, line)
	# unpack
	edges = edges_and_boxes[0]
	boxes = edges_and_boxes[1]


	if print_graph:
		# call plot and print, passing in nodes, edges, and boxes
		plot_and_print_graph(nodes, edges, boxes)
