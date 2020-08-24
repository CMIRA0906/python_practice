import requests

def create_user(dni,name,password): 
    #url='http://api.openweathermap.org/data/2.5/weather?q=London&appid=ec918468bb117cf178c12b82552db4cb'
    url='https://httpbin.org/post'
    dataPost={'dni':str(dni),'name':name,'password':password}
    response= requests.post(url,json=dataPost)
    print(response.text)
    return response


def get_user(dni):
    url='http://api.openweathermap.org/data/2.5/weather?q=London&appid=ec918468bb117cf178c12b82552db4cb'
    param={'dni':str(dni)}
    response= requests.get(url,params=param)
    print(response.text)
    return response

def check_created_user(dni,name,password):
    create_user(dni,name,password) 
    if (get_user(dni).status_code==200):
        print('El usuario fue creado correctamente')
    else:
        print('El usuario no fue creado')



check_created_user(1099,'camilo','cr123*')



