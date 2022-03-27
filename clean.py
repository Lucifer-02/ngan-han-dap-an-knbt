import bs4

file = open('raw_data.html', 'r', encoding='utf8')

html_raw_data = file.read()
file.close()

soup = bs4.BeautifulSoup(html_raw_data, 'html.parser')

questions = soup.find_all('div', class_='qtext')
answers = soup.find_all('div', class_='rightanswer')


file = open('clean_data.txt', 'w', encoding='utf8')
for i in range(len(questions)):
    file.write(questions[i].text + ';;;')
    file.write(answers[i].text + '\n')
