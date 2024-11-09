def __get_piece_positions(FEN_ROWS, FEN_PIECE, DESC=False):
	"""
	Find all of a FEN piece type and order them in binary.

	Args:
		FEN_ROWS: The FEN encoding as an array split on rows
		FEN_PIECE: The FEN encoding of the piece type
		DESC: order the respective pieces in decreasing order

	Returns:
		An array containing the binary representation of all positions of the given FEN piece type in DESC order.
	"""
	positions = []
	for i, row in enumerate(FEN_ROWS):
		for j, c in enumerate(row):
			if c == FEN_PIECE:
				positions.append((i * 8) + j)

	positions.sort(reverse=DESC)

	return positions

def get_all_positions(FEN_ROWS, DESC=False):
	"""
	Converts a FEN encoding of rows into binary representation of ordered pieces.

	Args:
		FEN_ROWS: The FEN encoding as an array split on rows
		DESC: order the respective pieces in decreasing order

	Returns:
		An array with two items:
			0) An array of arrays encoding each WHITE FEN piece type (KQRNBP) in order
			1) An array of arrays encoding each BLACK FEN piece type (kqrnbp) in order
	"""
	pieces = 'KQRNBP'

	white_positions = []
	black_positions = []
	for piece in pieces:
		# if DEBUG: print(piece)
		white_positions.append(__get_piece_positions(FEN_ROWS, piece))
		black_positions.append(__get_piece_positions(FEN_ROWS, piece.lower()))

	return [white_positions, black_positions]