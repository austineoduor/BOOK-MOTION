#!/usr/bin/env python3
from models.storage.db_storage import DBStorage
from models.user import User

user = User
st = DBStorage()
data_0 = {
    'username': 'maureen',
    'email': 'maureen@gmail.com',
    'password': 'pass',
    'first_name': 'maureen',
    'last_name': 'moreen'
    }
data_1 = {
    'username': 'austine',
    'email': 'austineoduor@gmail.com',
    'password': 'pass2',
    'first_name': 'austine',
    'last_name': 'oduor'
    }
data = [data_0, data_1]
if __name__ == '__main__':
    for d in range(len(data)):
        users = User(**data[d])
        st.save(users)
    print(users)
    #_id = ''
    #dat =list[st.get('User', _id)]
    #unwanted = '_sa_instance_state'
    #print(dat)
    
    #print(st.get('Book', _id))