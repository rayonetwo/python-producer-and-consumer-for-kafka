import json
import psycopg2
from kafka import KafkaConsumer

# Kafka Consumer 
consumer = KafkaConsumer(
    'messages',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest'
)

if __name__ == '__main__':
    try:
        for message in consumer:
            conn = psycopg2.connect('postgres://dumciori:yrmeE6B4Fw7xDBPc1YWvuc5MobnhUWXX@ruby.db.elephantsql.com/dumciori')
            cur = conn.cursor()
            parsed = json.loads(message.value)
            cur.execute("INSERT INTO messages (user_id, recipient_id, message) VALUES (%s, %s, %s)", (parsed["user_id"], parsed["recipient_id"], parsed["message"]))
            conn.commit()
            cur.close()
            conn.close()

    except Exception as e:
        print(str(e))
