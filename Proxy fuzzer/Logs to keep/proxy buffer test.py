import sys
import socket
import threading
import csv
import datetime

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode("utf-8", "ignore")
    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x}  {hexa:<{hexwidth}}  {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results


def receive_from(connection):
    buffer = b""
    connection.settimeout(15)
    try:
        while True:
            data = connection.recv(4096)#65535

            if not data:
                break

            buffer += data
    except Exception as e:
        print('error ', e)
        pass

    return buffer


def response_fuzz(buffer):
    # perform packet modifications
    return buffer


def proxy_handler(client_socket, remote_host, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print("[<==] Received %d bytes from local." % len(local_buffer))
            #local_buffer = b"\x10 \x00\x04MQTT\x04\xc2\x00<\x00\x00\x00\x08username\x00\x08password0\xf0\x9d\x85\xa0\x0e\x0b\xc0\x80\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT\x8e\xca\xb7\xb6MQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT-1\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/t\xe2\x81\xa9estMQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08d\xe2\x80\xabev/testMQTT0\x0e\x00\x08dev/testMQTT65535\x0e\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT8\x0e\x00\x08dev/testMQTT\xe0\x000"
            local_buffer = b"\x10 \x00\x04MQTT\x04\xc2\x00<\x00\x00\x00\x08username\x00\x08password0W\x00\x08d\xf3\xa0\x80\xbcev/testReceive normal data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal d\xf3\xa0\x81\x90ata (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the so\xca\xb6cket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.2147483647W\x00\x08dev/testReceive normes) and ancillary data from the s) and ancillary\xf3\xa0\x80\xac s) and ancillary data from the socket.\xe0\x00\x08"
            hexdump(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")

            local_buffer = b"\x10 \x00\x04MQTT\x04\xc2\x00<\x00\x00\x00\x08username\x00\x08password0W\x00\x08dev/testReceive normal data (upto bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.\xca\xb50W\x00\x08dev/testReceive normal data (up to bufsi\xe2\x80\x80ze byt\xf3\xa0\x80\xa3es) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.1W\x00\x08dev/testReceivery data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.-4052145382759568698611581049W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.\xf7d\xca\xb4L\xe0\xf3\xa0\x80\xb4\x00"
            hexdump(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")

            local_buffer = b"\x10 \x00\x04MQTT\x04\xc2\x00<\x00\x00\x00\x08username\x00\x08password0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data f\xf3\xa0\x81\x90rom the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsizeceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.53172W\x00\x08dev\xf3\xa0\x81\x85\xf3\xa0\x81\xbc/t) and acillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.0W\x00\x08dev/testReceive normal data (up to bufsize bytes) and ancillary data from the socket.\xe0\x00\xb5"
            hexdump(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote." % len(remote_buffer))
            #hexdump(remote_buffer)

            #remote_buffer = response_fuzz(remote_buffer)
            client_socket.send(remote_buffer)
            print("[==>] Sent to local.")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break


def server_loop(local_host, local_port, remote_host, remote_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print("[!!] Failed to listen on %s:%d" % (local_host, local_port))
        print("[!!] Check for other listening sockets or correct permissions.")
        print(e)
        sys.exit(0)

    print("[*] Listening on %s:%d" % (local_host, local_port))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        print("> Received incoming connection from %s:%d" % (addr[0], addr[1]))
        
        proxy_thread = threading.Thread(
            target=proxy_handler,
            args=(client_socket, remote_host,
                  remote_port))
        proxy_thread.start()


def main():
    if len(sys.argv[1:]) != 4:
        print("Usage: ./proxy.py [localhost] [localport]", end='')
        print("[remotehost] [remoteport]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000")
        sys.exit(0)
    
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    server_loop(local_host, local_port,
                remote_host, remote_port)


if __name__ == '__main__':
    main()
