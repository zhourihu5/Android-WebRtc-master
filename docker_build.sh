docker run --rm --name webrtc\
  -p 8081:8080 -p 8089:8089 -p 3478:3478 -p 3478:3478/udp -p 3033:3033 \
  --expose=59000-65000 \
  -e PUBLIC_IP=192.188.0.116 \
-v apprtc_configs:/apprtc_configs \
  -t -i piasy/apprtc-server