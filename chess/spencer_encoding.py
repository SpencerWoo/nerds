from utils import decimal_to_binary, binary_to_decimal

def __spencer_encode_white(white_positions):
	if DEBUG: print(white_positions)

	bits = []
	k = white_positions[0][0]
	k_in_b = decimal_to_binary(k)

	# ===
	# KING
	bits.append(k_in_b)

	# ===
	# POSITIONS
	# Q R N B
	for i in range(1, 5):
		q = white_positions[i]

		if len(q) == 0:
			bits.append(k_in_b)

		# one queen
		elif len(q) == 1:
			q_in_b = decimal_to_binary(q[0])
			bits.append(q_in_b)
			bits.append(q_in_b)

		# 2+ queens
		elif len(q) > 1:
			for i in range(len(q)-2):
				q_in_b = decimal_to_binary(q[i])
				bits.append(q_in_b)

			a, b = decimal_to_binary(q[len(q)-1]), decimal_to_binary(q[len(q)-2])

			bits.append(b)
			bits.append(a)

	return bits

def naive_spencer_encoding(positions):
	white_positions = positions[0]
	black_positions = positions[1]

	f = __spencer_encode_white(white_positions)
	return f