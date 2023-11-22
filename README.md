## Script to automate a creation of payload serialized to exploit java deserialization

ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --b64 --cmd whoami <br>
ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --gzp --cmd whoami <br>

--b64 : rO0 in Base64 <br>
--gzp : H4sIA" when gzip(base64)<br>
--cmd : command to exec<br>
--path : ysoserial-modified.jar path<br>


