def __get_piece_positions(FEN_ROWS, FEN_PIECE, DESC=False):
	positions = []
	for i, row in enumerate(FEN_ROWS):
		for j, c in enumerate(row):
			if c == FEN_PIECE:
				positions.append((i * 8) + j)

	positions.sort(reverse=DESC)

	return positions

def get_all_positions(FEN_ROWS):
	pieces = 'KQRNBP'

	white_positions = []
	black_positions = []
	for piece in pieces:
		# if DEBUG: print(piece)
		white_positions.append(__get_piece_positions(FEN_ROWS, piece))
		black_positions.append(__get_piece_positions(FEN_ROWS, piece.lower()))

	return [white_positions, black_positions]