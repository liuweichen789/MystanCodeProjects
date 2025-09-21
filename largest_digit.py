"""
File: largest_digit.py
Name: weichen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, find the maximum digit
	:return: int, the maximum digit
	"""
	num = 0
	return find_largest_digit_helper(n, num)


def find_largest_digit_helper(n, num):
	"""
	:param n: int
	:param num: the maximum digit
	:return: num
	"""
	if n < 0:  # 負數變成正數
		n = n * -1
	if n//10 < 1:  # base case: n剩1個數字
		if num < n:
			return n
		else:
			return num
	else:
		a = n % 10  # 取n的最後一位數字比較
		if num < a:
			num = a
		return find_largest_digit_helper(n//10, num)


if __name__ == '__main__':
	main()
