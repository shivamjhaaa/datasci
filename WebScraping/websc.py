import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
dataset = []
for i in range(1,2):
    response = requests.get(f'https://codeforces.com/problemset/page/{i}?order=BY_RATING_ASC' ,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    # print(soup)
    rows = soup.find_all('tr')
    for row in rows:
        problems = row.find_all('a',{'href': re.compile(r'^/problemset/problem/')})
        notices = row.find_all('a',{'class':'notice'})
        problemrating = row.find_all('span',{'class':'ProblemRating'})
        solved = row.find_all('a',{'title':'Participants solved the problem'})
        for problem in problems:
            print(problem.text.strip())
        for notice in notices:
            print(notice.text.strip())
        for rating in problemrating:
            print(rating.text.strip())
        for solve in solved:
            print(solve.text.strip())