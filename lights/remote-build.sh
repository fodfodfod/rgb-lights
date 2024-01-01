


CURRENT_WIFI_NAME="$(/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID:/{print substr($0, index($0, $2))}')"
TARGET_WIFI_NAME="SmartMesh"
if [ "$CURRENT_WIFI_NAME" == "$TARGET_WIFI_NAME" ]; then
	echo local
	scp -F ~/.ssh/config -r src myPI:/home/pi/rgb-lights/lights
	echo code deployed
	#ssh myPI "cd rgb-lights/lights; sudo cargo run"
else
	echo remote
	scp -F ~/.ssh/config -r src myPIremote:/home/pi/rgb-lights/lights
	echo code deployed
	#ssh myPIremote "cd rgb-lights/lights; sudo cargo run"
fi

#ssh myPIremote

