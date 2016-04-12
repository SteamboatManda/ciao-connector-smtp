# Ciao Connector SMTP
SMTP Connector for Arduino Ciao - Send email directly from your sketch

## Installation
### Linino OS
Open a `secure shell` to your board and login into **Linino OS**.
Install it via `opkg` running this commands:
```
$ opkg upgrade
$ opkg install ciao-connector-smpt
```

### Arduino OS
If you have **Arduino OS** installed in your
board you can use **Arduino Package Manager Application**.
Go to  *Menu -> Arduino -> Arduino Package Manger*
and then search `ciao-connector-smpt`, select it an press *Install*

## Manually
Download the zip file of the latest [release](https://github.com/arduino-org/ciao-connector-smtp/releases),
unzip and move it via `scp` inside you board in the desired location.
**Be sure to move `smtp.conf.json` file into the ciao directory**, eg:
```
$ scp /Users/sergio/Downloads/ciao-connector-smtp/smtp.conf.json root@arduino.local:/usr/lib/python2.7/ciao/conf/
$ scp -r /Users/sergio/Downloads/ciao-connector-smtp/smtp root@arduino.local:/root/.ciao/
```

## Configuration

### Ciao Core Configuration
Before start using the connector, set to `true` the `enabled` key.
Change the `commands/start` values only if you installed the connector manually.

```json
{
  "name" : "smtp",
  "enabled": false,
  "type" : "managed",
  "commands": {
          "start": ["/root/.ciao/smtp/smtp.py"],
          "stop": ["/usr/bin/killall","-s", "HUP","smtp.py"]
  },
  "implements" : {
          "write" : { "direction": "out", "has_params": true }
  }
}
```

### Connector Configuration/Parameters
To customize the connector to use your email account,
please insert the correct vaules in the configuration
file `smtp/smtp.json.conf`:

```json
...
"params" : {
  "host" : "SMTP_SERVER_HOST",
  "port" : SMTP_SERVER_PORT,
  "sender" : "SENDER EMAIL ADDRESS",
  "user" : "USERNAME",
  "password" : "PASSWORD",
  "ssl" : true,
  "tls" : true,
  "auth": true
},
...
```
example configuration for gmail:

```json
...
"params" : {
  "host" : "smtp.gmail.com",
  "port" : 465,
  "sender" : "youremail@gmail.com",
  "user" : "youremail@gmail.com",
  "password" : "yourpassword",
  "ssl" : true,
  "tls" : true,
  "auth": true
},
...
```


## How To Use
Open [Arduino IDE](http://www.arduino.org/software), import
Arduino Ciao Library in your sketch and take a look at the
[example](https://github.com/arduino-org/ciao-connector-smtp/examples)

## See Also
[Arduino Ciao](http://labs.arduino.org/Ciao)
