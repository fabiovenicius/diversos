import pickle
dbfile = open('c:\\temp\\people-pickle', 'rb')
db = pickle.load( dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
dbfile = open('c:\\temp\\people-pickle', 'wb')
pickle.dump( db, dbfile) 
dbfile.close()
