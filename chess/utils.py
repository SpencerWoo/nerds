def decimal_to_binary(num):
	"""
	Converts a decimal number to its binary representation.

	Args:
		num: The decimal number to convert.

	Returns:
		The binary representation of the number as a string.
	"""

	if num == 0:
		return '0'

	binary_string = ''
	while num > 0:
		remainder = num % 2
		binary_string = str(remainder) + binary_string
		num = num // 2

	return binary_string

def binary_to_decimal(binary_str):
	"""
	Converts a binary string to its decimal equivalent.

	Args:
		binary_str: The binary string to convert.

	Returns:
		The decimal equivalent of the binary string.
	"""

	decimal_num = 0
	power = 0

	for digit in reversed(binary_str):
		decimal_num += int(digit) * 2**power
		power += 1

	return decimal_num