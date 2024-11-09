from spencer_encoding import naive_spencer_encoding
from fen_encoding import get_all_positions

FEN_TEST = "r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1"
FEN_START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

SPENCER_ENCODING_BITS = []
DEBUG=True

def __convert_fen_to_spencer(FEN_ENCODED):
	FEN_ROWS = FEN_ENCODED.split("/")

	fen_positions = get_all_positions(FEN_ROWS)

	# TODO: preprocess fen_positions
	# then, depending on MVB determine which optimization to run
	
	# (1) naive
	spencer_encoded = naive_spencer_encoding(fen_positions)

	return spencer_encoded

if __name__ == "__main__":
	spencer_encoded = __convert_fen_to_spencer(FEN_START)
	print(spencer_encoded)