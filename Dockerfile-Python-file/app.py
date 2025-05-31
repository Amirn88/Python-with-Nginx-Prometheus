from flask import Flask
from prometheus_client import generate_latest, Counter, Gauge, REGISTRY

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
RANDOM_VALUE = Gauge('random_value', 'Randomly generated value')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello from metrics app!"

@app.route('/metrics')
def metrics():
    RANDOM_VALUE.set(REQUEST_COUNT._value.get() % 10)  # Simulate changing metric
    return generate_latest(REGISTRY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
