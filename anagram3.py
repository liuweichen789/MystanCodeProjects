"""
File: anagram.py
Name: wei chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    s: str, 請使用者輸入一單字。
    find_anagrams(s), 找出所有異序字.
    """
    start = time.time()
    ####################
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")

    while True:
        s = input('Find anagrams for: ')
        if s == '-1':
            break
        else:
            print('Searching...')
            find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    將檔案裡的單字，存在名為dic_lst的list裡面。
    """
    dic_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            dic_lst.append(line)
    return dic_lst


def find_anagrams(s):
    """
    :param s: str, user input
    :return: ans_lst, list, 所有異序字裝在ans_lst. counter[0], list, 異序字數量，
    """
    counter = [0]  # 有幾個anagrams。
    ans_lst = []   # 所有anagrams答案
    dic_lst = read_dictionary()  # 裝字典裡所有字的list
    find_anagrams_helper(s, '', len(s), ans_lst, counter, dic_lst, [])
    print(f'{counter[0]} anagrams: {ans_lst}')


def find_anagrams_helper(s, current_s, s_len, ans_lst, counter, dic_lst, current_index):
    """
    :param s: str, 使用者輸入之單字。
    :param current_s: str, 使用者輸入之單字的子母排列組合。
    :param s_len: int, 使用者輸入單字的單字長度。
    :param ans_lst: list, 所有找到的異序字。
    :param counter: list, 計算有幾個異序字。
    :param dic_lst: list, 裝字典中的字。
    :param current_index: int, 使用者輸入的單字，其字母排列組合的長度。
    :return: current_s, ans_lst
    """

    if len(current_index) == s_len:
        current_s = ''
        for j in current_index:  # TA: 只用index排字，字母不用重新backtracking
            current_s += s[j]
        if current_s in dic_lst:  # TA: 確認字有在字典裡，不是只是某單字的開頭
            if current_s not in ans_lst:
                ans_lst.append(current_s)
                counter[0] += 1
                print(f'Found: {current_s}')
                print('Searching...')
                # return current_s  # 為什麼字母backtracking不用return，做完就完成目前的stack frame了

    else:
        for i in range(s_len):  # TA:用index排字避免重複的字母被去掉 0,1 2, ...
            if i in current_index:
                pass
            else:
                # Choose
                # current_index += [i]  # 也是一樣的記憶體位址???
                # print(hex(id(current_index)))
                current_index.append(i)  # index排列組合
                # print(current_index)
                current_s = ''  # 字串依照index重新排，不然會累加之前排的
                for k in current_index:
                    # current_s = ''
                    current_s += s[k]  # 排完字，再確認是否是字首
                    # print(current_s)
                if has_prefix(current_s, dic_lst):
                    # explore
                    find_anagrams_helper(s, current_s, s_len, ans_lst, counter, dic_lst, current_index)
                # Un-choose
                current_index.pop()  # 不管排出的字是不是在字典裡，都要pop最後一個index，重新排
                # current_index = current_index[:-1]
                # print(hex(id(current_index)))
                # 為什麼不可以用current_index = current_index[:-1]。append的時候current_index是同一個記憶體位置，如果不是用pop，退回去的時候會製造不同記憶體位置的current_index。
                # 且只對當初append的current_index退最後的ele。


def has_prefix(sub_s, dic_lst):
    """
    :param sub_s: str, 字母排列片段
    :param dic_lst: list, 字典裡所有的單字。
    :return: sub_r有在字典裡為True，沒有為False
    """
    # dic_lst = read_dictionary()
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
