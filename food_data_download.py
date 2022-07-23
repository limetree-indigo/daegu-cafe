import requests

url = "https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr=수성구"

res = requests.get(url)

data = res.json()['data']

print(data)

with open('food_index_dg_suseong.txt', 'a', encoding='utf-8') as f:
    for d in data:
        line = ','.join([d['GNG_CS'],  d['FD_CS'],
                         d['BZ_NM'], d['MBZ_HR']])
        line += '\n'
        f.write(line)

with open('food_menu_dg_suseong.txt', 'a', encoding='utf-8') as f:
    for d in data:
        line = d['MNU'].split('<br />')
        line = [l.replace(',', '') for l in line]
        line = [l.strip() for l in line]
        line = ','.join(line)
        line += '\n'
        f.write(line)

