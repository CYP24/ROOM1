
wsdl_url = 'http://localhost:8000/?wsdl'
client = Client(wsdl=wsdl_url)

city = 'Lahti'
response = client.service.get_weather(city)

print(f"Weather Data: {response}")
