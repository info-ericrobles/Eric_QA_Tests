import requests
# Endpoint de prueba (Random User API)


# Prueba de API con requests
# Vamos a hacer una solicitud GET a una API pública.

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ API Test Passed")
    print(f"Nombre del usuario: {data['name']}")
else:
    print(f"❌ API Test Failed. Código de estado: {response.status_code}")

# Este script hace una petición GET y verifica si la API responde correctamente.