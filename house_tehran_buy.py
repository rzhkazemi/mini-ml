import requests
import re
for i in range(93, 201) :
    page_number = {'page' : i}
    url = 'https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86'
    response = requests.get (url, params = page_number )
    print(response.url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text , 'html.parser')
    ads = soup.find_all(class_ = 'list_infoBox__iv8WI p-2 align-self-center')
    for ad in ads :
        area_room_date_location_price_per_square_total_price = ad.find(class_= 'list_infoItem__8EH57 list_infoSpecs__EACNx d-flex'), ad.find(class_= 'list_infoItem__8EH57 ellipsis d-block').text , ad.find(class_ = 'list_infoItem__8EH57 list_infoPrice___aJXK d-block').text
        area_room_date = area_room_date_location_price_per_square_total_price[0].find_all(class_ = 'px-1 font-12')
        area =  int((re.findall(r'(\d*) متر',area_room_date[0].text))[0])
        try :
            number_of_room= int((re.findall(r'(\d*) خواب',area_room_date[1].text))[0])
        except IndexError :
            continue
        try: 
            construct_date = int(area_room_date[2].text)
        except IndexError: 
            continue
        location = re.findall(r'(\w*\s*\w*\s*\w*\s*)،{0,1} \s*تهران', area_room_date_location_price_per_square_total_price[1])[0]
        try :
            price_per_square = ad.find(class_ = 'list_infoItem__8EH57 font-14 global_colorGray1__i1u0y d-block')
        except IndexError:
            continue
        try :    
            price_per_square = int((re.findall(r'متری (\d*,{0,1}\d*,{0,1}\d*,{0,1}\d*) تومان',price_per_square.text)[0]).translate({ord(',') : None}))
        except AttributeError :
            continue
            
        try :
            total_price = int((re.findall(r'(\d*,{0,1}\d*,{0,1}\d*,{0,1}\d*) تومان',area_room_date_location_price_per_square_total_price[2]))[0].translate({ord(',') : None}))
        
        except IndexError:
            continue
        # print(location, area, number_of_room, construct_date, price_per_square, total_price)
        import mysql.connector 
            
        cnx = mysql.connector.connect(user = 'root', password = 'SlTuV5680M',
                                host = 'localhost', port = '3306',
                                database = 'property_db')
        cursor = cnx.cursor()
        cursor.execute('INSERT INTO property_info VALUES (\'%s\', \'%s\',\'%s\', \'%s\', \'%s\', \'%s\')' % (location, area, number_of_room, construct_date ,price_per_square, total_price))
        cnx.commit()
        cnx.close()

