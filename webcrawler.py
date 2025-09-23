"""
File: webcrawler.py
Name: wei chen
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': "t-stripe"})
        # print(tags)
        male_number = 0
        female_number = 0
        for tag in tags:
            # print(tag.text)
            target = tag.tbody  # tbody裡面有排名、名字、人數，還有空格
            # print(target.text)
            # print('-'*70)
            for td in target:
                # print(td.text)
                # print('-' * 70)
                data = td.text.split()
                # print(data)
                if len(data) == 5:
                    new_data = data  # 把空字串，其他字串去掉，只裝排名，名字，人數
                    new_data_list = []  # 要把整理後的token裝起來 <<< 整理後的token是不會assign回原本的new_data
                    for token in new_data:
                        token = string_manipulation(token)  # TA: 人數裡面有','不能直接轉int，要整理。
                        # print(token)
                        new_data_list.append(token)
                    # print(new_data_list)
                    # print('-' * 70)
                    male_number += int(new_data_list[2])
                    female_number += int(new_data_list[4])
            print('Male Number: ' + str(male_number))
            print('Female Number: ' + str(female_number))


def string_manipulation(s):
    """
    把字串裡面的標點符號或空格拿掉，只要數字與字母

    Args:
        s: str

    Returns: ans

    """
    ans = ''
    for ch in s:
        if ch.isdigit() or ch.isalpha():
            ans += ch
    return ans


if __name__ == '__main__':
    main()
