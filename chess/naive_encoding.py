def naive_encoding_worst_case():
	"""
	Naive math encoding of a chess position

	Returns:
		A maximal number of bytes to encode a chess position
	"""

	# 33 options
	# 64 positions

	num_bits = 33 ** 64
	num_bytes = num_bits/8
	print(num_bytes)
	# 1.9133841197731014e+96

# TODO: minimize via valid encodings only