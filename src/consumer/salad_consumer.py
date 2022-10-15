import json
from kafka import KafkaConsumer
from bs4 import BeautifulSoup


class SaladConsumer:
    def __init__(self):
        self.consumer = None

    def connect(self, topic_name):
        self.consumer = KafkaConsumer(
            topic_name,
            auto_offset_reset="earliest",
            bootstrap_servers=["localhost:9092"],
            api_version=(0, 10),
            consumer_timeout_ms=1000,
        )
        return self.consumer

    def parse(self, markup):
        rec = {}
        try:

            soup = BeautifulSoup(markup, "html.parser")
            # title
            title_section = soup.select("title")[0].contents[0]

            rec = {"title": title_section}

        except Exception as ex:
            print("Exception while parsing")
            print(str(ex))
        finally:
            return json.dumps(rec)

    def start_consumer(self, topic_name):
        consumer = self.connect(topic_name)
        for msg in consumer:
            html = msg.value
            result = self.parse(html)
            print(f"Message Received {result}")
