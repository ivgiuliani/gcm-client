Simple GCM command line client.


# Usage

```
./gcm.py <server api key> <registration token>
```

or

```
echo "{ JSON } " | ./gcm.py <server api key> <registration token>
```

## Example (send custom data):

```
echo '{"data": { "user": "username", "status": "connected" } }' | ./gcm.py "SERVER API KEY "REGISTRATION TOKEN" 
```

## Example (send a notification)

```
echo '{"notification": { "title": "This is a notification", "body": "I haven\'t wrote a single line of code client-side to send this notification and it just works! I\'m quite scared of the consequences.", "icon": "notification_icon", "color": "#900000" } }' | ./gcm.py "SERVER API KEY" "REGISTRATION TOKEN"

```
