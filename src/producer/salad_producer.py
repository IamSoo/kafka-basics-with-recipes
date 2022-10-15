from kafka import KafkaProducer


class KafkaSaladProducer:
    def __init__(self):
        self.producer = self.connect()

    def connect(self):
        producer = None
        try:
            producer = KafkaProducer(
                bootstrap_servers=["localhost:9092"], api_version=(0, 10)
            )
        except Exception as e:
            print(f"Error while connecting to kafka {e}")
        finally:
            self.producer = producer
            return producer

    def publish_message(self, producer, topic_name, key, value):
        try:
            key_bytes = bytes(key, encoding="utf-8")
            value_bytes = bytes(value, encoding="utf-8")
            producer.send(topic_name, key=key_bytes, value=value_bytes)
            producer.flush()
            print(f"Message Published successfully")
        except Exception as e:
            print(f"Error while publishing the message {e}")

    def produce_salad_recipe(self, recipes, topic_name):
        k_producer = KafkaSaladProducer()
        producer = k_producer.connect()
        for recipe in recipes:
            k_producer.publish_message(producer, topic_name, "raw", recipe.strip())
