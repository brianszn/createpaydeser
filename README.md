## Script to automate a creation of payload serialized to exploit java deserialization

ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --b64 --cmd whoami
ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --gzp --cmd whoami

--b64 : rO0 in Base64
--gzp : H4sIA" when gzip(base64)
--cmd : command to exec
--path : ysoserial-modified.jar path


