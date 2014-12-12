
import sqlite3

createDb = sqlite3.connect(':memory:')

queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''CREATE TABLE customers
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL)''')

def addCust(name,street,city,state,balance):
    queryCurs.execute('''INSERT INTO customers (name,street,city,state,balance)
    VALUES (?,?,?,?,?)''',(name,street,city,state,balance))
    


def main():
    createTable()
    addCust('Customer1 Lastname','12345 Highway', 'Enola', 'PA', 123.45)
    addCust('Customer2 Lastname','14245 Highway', 'Enola',  'PA', 45.40)
    addCust('Customer3 Lastname','12225 Highway', 'Enola', 'PA', 1000.50)
    addCust('Customer4 Lastname','7777 Highway', 'Enola', 'PA', 1203.20)
    
    createDb.commit()
    
    queryCurs.execute('SELECT * FROM customers')
    listTitle = ['Id Num', 'Name ', 'Street ', 'City ', 'State ', 'Balance ']
    k = 0
    for i in queryCurs:
        print "\n"
        for j in i:
            print listTitle[k],
            print j
            if k < 5:
                k += 1
            else:
                k = 0
    
    queryCurs.close()
    



if __name__ == '__main__': main()


    
