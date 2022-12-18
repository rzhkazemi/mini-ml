from sklearn import tree
import requests 
import re
from bs4 import BeautifulSoup
import mysql.connector
location = input('location: ')
cnx = mysql.connector.connect(user = 'root', password = 'SlTuV5680M',
                                            host = 'localhost', port = '3306',
                                           database = 'property_db')

query = ("SELECT DISTINCT * From property_info WHERE location like N'%s'" % location)
cursor = cnx.cursor()
cursor.execute(query)
selected_list = []
for location, area, number_of_room, construct_date, price_per_square, total_price in cursor :
    selected_case = area, number_of_room, construct_date, price_per_square, total_price
    selected_list.append(selected_case)

x = []
y = []
for item in selected_list :
    x.append(item[0:3])
    y.append(item[3:5])
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
new_data = [(90, 2, 1389), (200, 4, 1395)]
expectation = clf.predict(new_data)
print(expectation[0])
print(expectation[1])
cnx.close()
        