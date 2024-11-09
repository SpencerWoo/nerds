def egg_drop(eggs, floors):
		dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

		# Base cases
		for i in range(1, eggs + 1):
				dp[i][1] = 1
		for j in range(1, floors + 1):
				dp[1][j] = j

		# Fill the dp table
		for i in range(2, eggs + 1):
				for j in range(2, floors + 1):
						dp[i][j] = float('inf')
						for k in range(1, j + 1):
								dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))

		# print(dp)

		return dp[eggs][floors]

total_floors = 1000
num_eggs_tests = [1, 2, 3, 4, 5]
for num_eggs in num_eggs_tests:
	print(egg_drop(num_eggs, total_floors))