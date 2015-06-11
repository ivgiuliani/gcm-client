Simple GCM command line client.


# Usage

```
./gcm.py <server api key> <registration token>
```

or

```
echo "{ JSON } " | ./gcm.py <server api key> <registration token>
```

## Example:

```
echo '{"data": { "user": "username", "status": "connected" } }' | ./gcm.py "SERVER API KEY "REGISTRATION TOKEN" 
```
