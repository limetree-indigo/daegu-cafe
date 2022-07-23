from collections import defaultdict
from pprint import pprint

def get_data():
    with open('food_index_dg_suseong.txt', encoding='utf-8') as f:
        data_index = f.readlines()

    with open('food_menu_dg_suseong.txt', encoding='utf-8') as f:
        data_menu = f.readlines()

    data_index = [d.replace('\n', '') for d in data_index]
    data_index = [d.split(',') for d in data_index]

    korean = ['퓨전/뷔페', '디저트/베이커리', '한식', '일식', '전통차/커피전문점', '양식', '세계요리', '중식']
    english = ['fusion-buffet', 'desert-bakery', 'korean', 'japanese', 'tea-coffee', 'western', 'global', 'chinese']

    for i, d in enumerate(data_index):
        idx = korean.index(d[1])
        data_index[i][1] = english[idx]

    data_menu = [d.replace('\n', '') for d in data_menu]
    data_menu = [d.split(',') for d in data_menu]

    data = []
    head = ['주소', '종류', '가게명', '영업시간']
    for i, m in zip(data_index, data_menu):
        store = dict()
        store = {k:v for k, v in zip(head, i)}
        store['메뉴'] = m
        data.append(store)

    # 맛집 종류별로 데이터 정리
    categories = defaultdict(list)
    for d in data:
        categories[d['종류']].append(d)

    categories = list(categories.items())

    return tuple(zip(categories, korean))


if __name__ == "__main__":
    result, kor = get_data()
    for c in result:
        print(c[0], end=' ')
    print()
    print(kor)


