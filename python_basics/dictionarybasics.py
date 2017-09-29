me = {
    'name': 'Hieu',
    'age': 26,
    'country': 'Vietnam',
    'language': 'Sarcasm'
}
def aboutMe():
    print """
    My name is %s
    My age is %s
    My country of birth is %s
    My favorite language is %s
    """ % (me['name'], me['age'], me['country'], me['language'])
aboutMe()