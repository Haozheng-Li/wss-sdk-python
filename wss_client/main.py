# WSS client
import communicate
import performance

API_KEY = ''
WEBSOCKET_URL = "wss://wssweb.net/ws/device/{api_key}"

ws_obj = communicate.init_websocket_client(WEBSOCKET_URL.format(api_key=API_KEY))
monitor = performance.get_performance_monitor()
monitor.set_interval(1)  # Upload device running status data per 1s
monitor.start()

# Your other logic
while True:
    pass

