from pymongo import MongoClient

conn = MongoClient()
collection = conn.phone_identification.data

f = open('phone.log', 'w', encoding='utf-8')

for item in collection.find(no_cursor_timeout=True):
    phone = item.get('phone', '')
    isSuccess = item.get('isSuccess', False)
    if phone.startswith('186') and isSuccess:
        f.write(phone + '\n')
        print(phone)
    print('down！')
f.close()
