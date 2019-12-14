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
name= input('Name :')
request = input('Phone numbers(p) or address(a)?')
if request == 'p': print("{}'s phone number is {}".format(name,people[name]['phone']))
if request == 'a': print("{}'s address is {}".format(name,people[name]['addr']))

