# initialize data to be stored in files, pickles, shelves 
# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
fabio = {'name':'Fabio Reis','age':38,'pay':50000,'job':'man'}
thiago = {'name':'Thiago Amorim','age':36,'pay':10000,'job':'hdw'}
# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db['fabio']=fabio
db['thiago']=thiago

if __name__ == '__main__': 
# when run as a script 
    for key in db: 
        print(key, '= >\ n ', db[key])
