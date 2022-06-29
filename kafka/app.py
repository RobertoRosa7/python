from kafka import KafkaProducer, KafkaConsumer

class NewOrderMain:

  def __initi__(self):
    pass
  
  def main(self):
    key = b'1234'
    value = b'teste'
    producer = KafkaProducer(bootstrap_servers=["http://192.168.1.25:9092"], api_version=(1, 0, 0))
    producer.send('ECOMMERCE_NEW_ORDER', key=key, value=value)
    future = producer.send('ECOMMERCE_NEW_ORDER', key=key, value=value)

    # consumers = KafkaConsumer('ECOMMERCE_NEW_ORDER')
    result = future.get(timeout=60)
    print("Topic => {}".format(result.topic))
    print("Partition => {}".format(result.partition))
    print("Offset => {}".format(result.offset))
    print("TimeStamp => {}".format(result.timestamp))


NewOrderMain().main()