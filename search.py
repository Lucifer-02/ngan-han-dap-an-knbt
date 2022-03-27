file = open('clean_data.txt', 'r', encoding='utf8')

data = file.read().split('\n')

print(len(data))

for i in range(len(data)):
    data[i] = data[i].split(';;;')

while(True):
    key = input('Enter key: ')
    print('\033[93m' + '----------------------------------------------------------------------------------------------------------------')
    for i in range(len(data)):
        if data[i][0].find(key) != -1:
            print('\033[36m' + 'Đáp án: ' + '\033[92m' + data[i][1].replace('Câu trả lời đúng là:',''))
    print('\033[93m' + '----------------------------------------------------------------------------------------------------------------')
