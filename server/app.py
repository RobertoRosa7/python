# -*- coding: utf-8 -*-
import socket
import subprocess

# definition credentials
credentials = ['root:123456', 'root:toor', 'admin:123456']

# doing connection to internet
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# transmitir conexão para qualquer host
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# definition address of server and port
addressServer = ('127.0.0.1', 8080)

sock.bind(addressServer)

# subir servidor com maximo de conexões
sock.listen(5)

# conexão persistente
while True:
    connection = sock.accept()
    addressClient = sock.accept()
    print("[*] New connection from {0}:{1}".format(*addressClient))
    try:
        connection.send(b'Username: ')
        username = connection.recv(32).strip().decode('utf-8')
        connection.send(b'Password: ')
        passowrd = connection.recv(32).strip().decode('utf-8')

        if "{0}:{1}".format(username, password) in credentials:
            connection.send(b'\nWelcome to socket server\n')

            while True:
                connection.send(b'$ ')
                data = connection.recv(1024).strip().decode('utf-8')

                if data == 'exit':
                    break
                if data == 'shell':
                    while True:
                        connection.send(b'SHELL: ')
                        datapoint = connection.recv(2048)
                        proc = subprocess.Popen(datapoint, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdoutValue = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                        connection.send(stdoutValue)

                if data == 'server info':
                    cmdServer = 'uname -a'
                    proc = subprocess.Popen(cmdServer, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdoutValue = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                    connection.send(stdoutValue)

                else:
                    connection.send(b'command not found: ' + data + b'\n')
        else:
            connection.send(b'Access denied')
    except socket.error:
        print('An error occured with ip = {0}, port = {1} client: '.format(*addressClient))
    finally:
        connection.close()
