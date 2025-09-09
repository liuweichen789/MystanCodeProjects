"""
File: boggle.py
Name: wei chen
----------------------------------------
適用者輸入4行各4個字母，共得16個字母，取每個字母與其相鄰的字母排列成異序字。
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	將使用者輸入的字母，依行數與次序為字母的位置，編座標，座標為key，字母為value，用dictionary裝起來，再取字母相鄰的字，排列成異序字。
	"""
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')

	input_dic = {}  # 將字母依位置編上座標，key:val = (j, i): letter
	for i in range(4):  # 使用者輸入4行字母
		s = input(str(i + 1) + ' row of letters: ')
		new_s = ''  # 整理使用者輸入之字串，去掉空格並將所有字母變小寫
		if len(s) > 7:
			print('Illegal input')
			break
		else:
			for j in range(4):  # 每行有4個字母
				for ch in s:
					if ch.isalpha():
						new_s += ch.lower()
				input_dic[j, i] = new_s[j]

	if len(input_dic) == 16:
		print(input_dic)
		find_anagrams(input_dic)
		# current_letter = []
		# ans_lst = []
		# for i in range(4):
		# 	for j in range(4):
		# 		current_letter += j, i
		# 		find_anagrams(input_dic, current_letter, ans_lst)
		# 		current_letter = []  # 一個字母選完，就清除list，放入下一個字母的座標
		# print(f'There are {len(ans_lst)} words in total')


def find_anagrams(input_dic):
	"""
	:param input_dic: dictionary, 使用者輸入之字母，字母座標為key，字母為value。
	:return: string
	"""
	dictionary_lst = read_dictionary()
	ans_lst = []  # 裝所有異序字
	current_lst = []  # 裝正在排列的座標
	current_letter = []  # 每次取1個字母，進入find_anagrams_helper()
	# find_anagrams_helper(input_dic, '', ans_lst, dictionary_lst, [], current_letter)
	for i in range(4):
		for j in range(4):
			current_letter += j, i
			find_anagrams_helper(input_dic, '', ans_lst, dictionary_lst, [], current_letter)
			current_letter = []  # 一個字母選完，就清除list，放入下一個字母的座標
	print(f'There are {len(ans_lst)} words in total')


def find_anagrams_helper(input_dic, current_s, ans_lst, dictionary_lst, current_lst, current_letter):
	"""
	:param input_dic: 使用者輸入之字母，座標與字母之dictionary
	:param current_s: str,排列中的字串
	:param ans_lst: list, 裝所有答案的list
	:param dictionary_lst: 裝字典裡所有的字的list
	:param current_lst: list, 排列中的座標
	:param current_letter: list, 每次取1個字母，開始排列
	:return: current_s, str, 異序字。ans_lst, list,所有異序字答案
	"""

	j = current_letter[0]
	i = current_letter[1]
	for x in range(j-1, j+2):  # 取周圍的字母
		for y in range(i-1, i+2):
			if 0 <= x <= 3 and 0 <= y <= 3:
				# print(f'current_letter= {current_letter}')
				# print(f'current_lst = {current_lst}')
				if (x, y) in current_lst:
					pass
				else:
					# choose
					current_lst.append((x, y))  # TA: 用current_lst += x,y會變成list，不是tuple
					current_s = ''
					for t in current_lst:
						current_s += input_dic[t]  # 把座標所代表的字母排入字串
					if has_prefix(current_s, dictionary_lst):
						if len(current_s) >= 4:
							if current_s in dictionary_lst:
								if current_s not in ans_lst:
									ans_lst.append(current_s)
									print(f'Found "{current_s}"')
						# explore
						find_anagrams_helper(input_dic, current_s, ans_lst, dictionary_lst, current_lst, current_letter)
					# un-choose
					current_lst.pop()


def read_dictionary():
	"""
	:return: dictionary, list, 裝字典裡所有的字的list
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			dictionary_lst.append(line)
	return dictionary_lst


def has_prefix(sub_s, dictionary_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary_lst: list, 裝字典裡，所有的單字
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
