#TURN_BASE_URL = 'https://computeengineondemand.appspot.com'
TURN_BASE_URL = 'http://192.188.0.116:3478'
TURN_URL_TEMPLATE = '%s/turn?username=%s&key=%s'
# TURN_URL_TEMPLATE = '%s/turn.php?username=%s&key=%s'
CEOD_KEY = '4080218913'
# CEOD_KEY = '1234'

WSS_INSTANCES = [{
    #WSS_INSTANCE_HOST_KEY: 'apprtc-ws.webrtc.org:443',
    WSS_INSTANCE_HOST_KEY: '192.188.0.116:443',
    WSS_INSTANCE_NAME_KEY: 'wsserver-std',
    WSS_INSTANCE_ZONE_KEY: 'us-central1-a'
}, {
    #WSS_INSTANCE_HOST_KEY: 'apprtc-ws-2.webrtc.org:443',
    WSS_INSTANCE_HOST_KEY: '192.188.0.116:443',
    WSS_INSTANCE_NAME_KEY: 'wsserver-std-2',
    WSS_INSTANCE_ZONE_KEY: 'us-central1-f'
}]