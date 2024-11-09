def naive_encoding_worst_case():
	# 33 options
	# 64 positions

	num_bits = 33 ** 64
	num_bytes = num_bits/8
	print(num_bytes)
	# 1.9133841197731014e+96

# TODO: minimize via valid encodings only