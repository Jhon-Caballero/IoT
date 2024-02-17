import requests
url= 'https://script.google.com/macros/s/AKfycbxol8Wh4lnCFAgHfIefccip0T-qQsZbnge1SsETJ3GVSdxpDvg18yBhcT3gTO92yO04YA/exec'

# Ojo: este es un diccionario. No confundir con JSON
cargaUtil={'nevera':'DoñaNancy','producto':'tomate','cantidad':'5','pesos':'50000'}
respuesta = requests.post(url, data=cargaUtil)
print(respuesta.text)
print("La URL usada en el POST es: ", respuesta.request.url)