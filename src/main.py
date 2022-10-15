from producer.salad_producer import KafkaSaladProducer
from consumer.salad_consumer import SaladConsumer
from scraper.scraper import SaladScraper
from config.config import Config

if __name__ == "__main__":
    confg = Config()
    data = confg.load_config()
    topic = data["topic"]["raw"]

    scraper = SaladScraper()
    scraped_recipes = scraper.scrape()

    producer = KafkaSaladProducer()
    producer.produce_salad_recipe(scraped_recipes, topic)

    consumer = SaladConsumer()
    consumer.start_consumer(topic)
