import paho.mqtt.client as mqtt

broker = "mqtt.eclipse.org"
port = 1883
topic = "simulacao/ataques/mqtt"
client_id = "subscritor_simulacao"

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()}")

client = mqtt.Client(client_id)
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
client.loop_forever()
