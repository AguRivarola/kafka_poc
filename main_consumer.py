import json
from quixstreams import Application

def main():
    app = Application(
        broker_address="kafka:9092",
        loglevel="DEBUG",
        consumer_group="weather_reader",
        auto_offset_reset="latest"
    )


    with app.get_consumer() as consumer:
        consumer.subscribe(["weather_data_demo"])

        while True:
            msg = consumer.poll(1)

            if msg is None:
                print("Waiting...")
            elif msg.error() is not None:
                raise Exception(msg.error())
            else:
                key = msg.key().decode('utf8')
                value = json.loads(msg.value()) 
                offset = msg.offset()
                consumer.store_offsets(msg)
                print(f"{offset} {key} {value}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass