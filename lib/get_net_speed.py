import speedtest

class NetSpeed:

  def __init__(self):
    speedTestHelper = speedtest.Speedtest()

    speedTestHelper.get_best_server()

    # Check download speed
    speedTestHelper.download()

    # Check upload speed
    speedTestHelper.upload()

    # serialize result
    self.result = self.serialize_test(speedTestHelper.results.dict())

  def serialize_test(self, speed):
    output = {}
    output['download'] = f"{round(speed['download']/1000000, 2)} mbps"
    output['upload'] = f"{round(speed['upload']/1000000, 2)} mbps"
    output['ping'] = f"{speed['ping']} ms"
    output['data_sent'] = f"{round(speed['bytes_sent'] / 2**20, 2)} MB"
    output['data_received'] = f"{round(speed['bytes_received'] / 2**20, 2)} MB"
    return output
