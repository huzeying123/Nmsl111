people = {

    'hzy': {
        'phone':'1234',
        'addr':'ucas 23',
    },
    'hjy':{
        'phone':'1233',
        'addr':'ucas 24',
    },
    'msn':{
        'phone':'1238',
        'addr':'ucas 25'
    },
}
labels= {
    'phone':'phone number',
    'addr':'address',
}
name= input('Name :')
request = input('Phone numbers(p) or address(a)?')
key = request
if request == 'p':key='phone'
if request == 'a':key='addr'
person= people.get(name,{})
print(person)
label = labels.get(key,request)
result = person.get(key,'not available')
print("{}'s {} is {}".format(name, label, result))
