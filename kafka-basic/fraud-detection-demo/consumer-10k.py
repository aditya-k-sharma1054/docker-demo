from kafka import KafkaConsumer
import json

print("=== Starting 10K Fraud Monitor ===")
consumer = KafkaConsumer(
    'fraud-notification',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    alert_data = message.value
    amount = alert_data.get('amount', 0)
    
    # Strictly filter for amounts over 10,000
    if amount > 10000.0:
        print(f"\n🚨 [CRITICAL ALERT > $10,000]")
        print(f"User: {alert_data.get('userId')} ({alert_data.get('name')})")
        print(f"Amount: ${amount:.2f} | Tx ID: {alert_data.get('tx_id')}")
