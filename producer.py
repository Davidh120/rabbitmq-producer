import time
import pika
import json
import random

# Genera una ubicación aleatoria con latitud y longitud
def generate_random_location():
    latitude = random.uniform(-90.0, 90.0)
    longitude = random.uniform(-180.0, 180.0)
    return {
        "latitude": latitude,
        "longitude": longitude
    }

def main():
    # Establece una conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declara la cola a la que se enviarán los mensajes
    channel.queue_declare(queue='queue1', durable=True, exclusive=False, auto_delete=True)

    # Genera y envía 10 ubicaciones aleatorias a la cola
    for _ in range(10):
        location = generate_random_location()
        channel.basic_publish(exchange='', routing_key='queue1', body=json.dumps(location))
        time.sleep(1)

    # Cierra la conexión
    connection.close()

if __name__ == '__main__':
    main()
