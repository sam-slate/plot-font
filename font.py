# based off of: https://orig09.deviantart.net/6091/f/2013/120/f/c/5x5_textfont_by_truearena111-d63ele8.png

left = [(0, 0), (0, 5), (1, 0), (1, 5)]
right = [(4, 0), (5, 0), (4, 5), (5, 5)]
top = [(0, 4), (0, 5), (5, 5), (5, 4)]
bottom = [(0, 0), (0, 1), (5, 0), (5, 1)]
mid_vertical = [(2, 0), (3, 0), (2, 5), (3, 5)]
mid_horizontal = [(0, 2), (0, 3), (5, 2), (5, 3)]
diagonal_down = [(0, 5), (1, 5), (4, 0), (5, 0)]
left_mid_to_top_right = [(0, 2), (1, 2), (4, 5), (5, 5)]
left_mid_to_bottom_right = [(0, 3), (1, 3), (4, 0), (5, 0)]
bottom_half_mid_vertical = [(2, 0), (3, 0), (2, 3), (3, 3)]
mid_mid_to_top_left = [(2, 2), (3, 2), (0, 5), (1, 5)]
mid_mid_to_top_right = [(2, 2), (3, 2), (4, 5), (5, 5)]
top_except_top_left = [(1, 4), (1, 5), (5, 4), (5, 5)]
bottom_except_bottom_right = [(0, 0), (0, 1), (4, 0), (4, 1)]
mid_three_horizontal = [(1, 2), (1, 3), (4, 2), (4, 3)]
s_small_pieces = [[(3, 0), (4, 0), (4, 2), (5, 2)], [(4, 1), (5, 1), (3, 3), (4, 3)], [(1, 2), (2, 2), (0, 4), (1, 4)], [(0, 3), (1, 3), (1, 5), (2, 5)]]
diagonal_down_top_three = [(0, 5), (1, 5), (2, 2), (3, 2)]
diagonal_up_top_three = [(2, 2), (3, 2), (4, 5), (5, 5)]



font = {
	'T': [mid_vertical, top],
	'H': [left, mid_horizontal, right],
	'A': [left, right, mid_horizontal, top],
	'N': [left, right, diagonal_down], 
	'K': [left, left_mid_to_top_right, left_mid_to_bottom_right],
	'Y': [bottom_half_mid_vertical, mid_mid_to_top_right, mid_mid_to_top_left],
	'O': [top, left, right, bottom],
	'U': [left, right, bottom],
	'S': [top_except_top_left, bottom_except_bottom_right, mid_three_horizontal] + s_small_pieces,
	'M': [left, right, diagonal_up_top_three, diagonal_down_top_three],
	'L': [left, bottom],
	'E': [left, top, mid_horizontal, bottom],
	'I': [top, bottom, mid_vertical],
	'C': [top, left, bottom],
	'F': [top, mid_horizontal, left]
	' ': []
}

