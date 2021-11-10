import time
import json
from lib.get_net_speed import NetSpeed
from lib.logstash import Logstash

speed_test_repeat = 3600

logger = Logstash()

logger.log_and_print('speed test app starting up')

while True:
	start_time = time.time() 
	print('running speed test now')
	speed = NetSpeed()
	output = speed.result
	logger.log_and_print(json.dumps(output))
	test_time = round(time.time() - start_time, 2) 
	print(f"speed test took {test_time} seconds")
	sleep_time = round(speed_test_repeat - test_time, 2) 
	print(f"sleeping {sleep_time} seconds")
	time.sleep(sleep_time)
