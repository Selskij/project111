from faker import Faker
import json
dict = {}
fake_ru = Faker('en_US')

for i in range (250):
    name = fake_ru.name()
    tn = fake_ru.phone_number()
    j = fake_ru.job()
    A = fake_ru.address()
    dict[i]={i:[name,tn,j,A]}
    with open ('DS.txt', 'w', encoding = 'utf8') as f:
        json.dump(dict,f,indent=4,ensure_ascii=False)


def argu():
    """This function is......"""
    ...


def fr():
    '''This func...'''
    ...

print(__name__)
print(argu.__doc__)


