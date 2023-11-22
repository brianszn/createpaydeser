# createpaydeser
Script to automoate a creation of payload serialize to exploit java deserialization

Java serialized payload generator 
	 github.com/brianszn 

ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --b64 --cmd whoami
ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --gzp --cmd whoami

obs: "ysoserial-modified.jar" default name of ysoserial jar archive in the path.
obs: Payloads converted in URL.

options:
   -h, --help   show this help message and exit
   
   --b64        rO0 in Base64
   --gzp        H4sIA" when gzip(base64
   --path PATH  ysoerial-modified.jar Path
   --cmd CMD    command to exec
