from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer(
        "com.udacity.cf",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset='earliest', 
        enable_auto_commit=False
    )
    for msg in consumer:
        if msg is not None:
            print(msg.value.decode('utf-8'))
            
if __name__ == "__main__":
    main()