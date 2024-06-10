import paho.mqtt.client as mqtt
import time

broker = "mqtt.eclipse.org"
port = 1883
topic = "simulacao/ataques/mqtt"
client_id = "publicador_simulacao"

def on_publish(client, userdata, result):
    print("Dados publicados \n")
    pass

client = mqtt.Client(client_id)
client.on_publish = on_publish
client.connect(broker, port)

while True:
    message = input("Digite a mensagem para publicar: ")
    result = client.publish(topic, message)
    time.sleep(1)
