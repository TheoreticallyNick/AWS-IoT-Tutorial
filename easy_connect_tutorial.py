import json
import AWSIoTPythonSDK.MQTTLib
from AWSIoTPythonSDK.MQTTLib import *

class MQTTParams:
    ### This class creates an object with the appropriate pointers to the permission files required by aws

    def __init__(self):
        
        # aws host address
        self.host = "xxxxxxxx.amazonaws.com"
        # path to root-ca file
        self.rootCAPath = "/path/to/root-CA.crt"
        # path to certificate file
        self.certificatePath = "/path/to/test.cert.pem"
        # path to the private key file
        self.privateKeyPath = "/path/to/test.private.key"
        # port number (do not change)
        self.port = 8883
        # client ID name (can be any string)
        self.mqttClientId = "test"

mqtt = MQTTParams()

### The following sets up the connection parameters to the MQTT client broker on aws using the certificates from MQTT param class object
myAWSIoTMQTTClient = AWSIoTMQTTClient(mqtt.mqttClientId)
myAWSIoTMQTTClient.configureEndpoint(mqtt.host, mqtt.port)
myAWSIoTMQTTClient.configureCredentials(mqtt.rootCAPath, mqtt.privateKeyPath, mqtt.certificatePath)
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myAWSIoTMQTTClient.configureOfflinePublishQueueing(3, AWSIoTPythonSDK.MQTTLib.DROP_OLDEST)

### connects to aws MQTT broker
result = myAWSIoTMQTTClient.connect()

### MQTT broker topic
topic = "test"

### messages payload, must be in json format
JSONpayload = json.dumps({'name': "device", 'msg': "message from device"})

### publish function
myAWSIoTMQTTClient.publish(topic, JSONpayload, 1) 