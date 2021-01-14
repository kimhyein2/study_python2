# p.88 딕셔너리 자료형

dic = {
    # key   #vlaue
    'name': 'pey',
    'phone': '0119993323',
    'birth': 'female',
    'job': 'artist'
}

# dic['age'] = 25
# del dic['job']
# del dic['phone']
# print(dic)

# for key in dic:
#     print(key, ':', dic[key])
# 빈 딕셔너리
dic2 = {}
dic2['name']='john'
dic2['phone']='0103334454'
dic2['birth'] = '0815'
dic2['gender'] = 'male'
dic2['job'] = 'developer'

#키 추출
dic_keys = dic.keys()
#값 추출
dic_values = dic.values()
#키, 값 모두 추출
dic_key_value = dic.items()

#print(dic_keys, type(dic_keys))
# print(dic_key_value, type(dic_key_value))
# for key,value in dic_key_value:
#     print(f'{key} : {value}')

athlete = ['김연아','손흥민','류현진','박세리','손연재']
category = ['피겨스케이팅','축구','야구','골프','리듬체조']

total = {}

for i in range(len(athlete)):
    total[i] = category[i]
print(total)



