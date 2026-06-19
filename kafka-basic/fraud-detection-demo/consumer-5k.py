from kafka import KafkaConsumer
import json

print("=== Starting 5K Warning Monitor ===")
consumer = KafkaConsumer(
    'fraud-notification',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    alert_data = message.value
    amount = alert_data.get('amount', 0)
    
    # Filter for mid-tier transactions ($5,000 to $10,000)
    if 5000.0 <= amount <= 10000.0:
        print(f"\n⚠️ [WARNING ALERT $5,000 - $10,000]")
        print(f"User: {alert_data.get('userId')} ({alert_data.get('name')})")
        print(f"Amount: ${amount:.2f} | Tx ID: {alert_data.get('tx_id')}")
