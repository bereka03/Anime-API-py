import requests
import json
import sqlite3

# anime_name = input("შეიყვანეთ ანიმეს სახელი: ")
# url = f"https://anime-facts-rest-api.herokuapp.com/api/v1/{anime_name}"
# r = requests.get(url)
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print((r.content))
# data = r.json()
# print(data)
# with open ('data.json', 'w') as file:
#     json.dump(data, file, indent=4)
# file.close()
# img = requests.get(data['img'])
# img_content = img.content
# with open('anime.png', 'wb') as file2:
#     file2.write(img_content)
# file2.close()
# data_json = json.dumps(data, indent=4) # dict-ის მსგავსად წარმოჩენა
# print(data_json)
# total_facts = data['total_facts']
# print(total_facts)
# fact_13 = data['data'][12]
# print(fact_13)  # მეცამეტე ფაქტის გამოტანა

# API ინფორმაცაიის ბაზაში შენახვისთვის
url2 = "https://anime-facts-rest-api.herokuapp.com/api/v1"
r2 = requests.get(url2)
data2 = r2.json()
data2_json = json.dumps(data2, indent=4)
# print(data2_json)

conn = sqlite3.connect('anime_db.sqlite')  # ბაზასთან დაკავშირება (ჩვენს შემთხვევასი შექმნა ახალი ბაზის)
c = conn.cursor() # კურსორის შექმნა
# ცხრილის შექმნა
c.execute('''CREATE TABLE IF NOT EXISTS anime   
           (id INTEGER  PRIMARY  KEY  AUTOINCREMENT,
            title VARCHAR(40),
            img_url VARCHAR(1000)) ''')

my_list = []
for each in data2['data']:
    content = each.values()
    my_list.append(tuple(content))
print(my_list)

c.executemany("INSERT INTO anime (id, title, img_url) values (?, ?, ?)", my_list) # sql placeholder ინფორმაციის დამატება
records = c.fetchall()
conn.commit()  # ცვლილების დაქომითება რათა აისახოს ბაზაში ცვლილება
conn.close()
