import sys
import socket
import threading
import csv
import datetime
import pyradamsa

rad = pyradamsa.Radamsa()

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def write_to_file(original):
    with open("publisher_log_proxy.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), original, "MESSAGE NOT FUZZED"])
def write_to_file_c(original, case):
    with open("publisher_log_proxy.csv", 'a', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.datetime.now(), original, case])

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
        #buffer = connection.recv(4096)
        counter = 1
        while True:
            data = connection.recv(4096)
            print("---")
            print(data)
            print("^^^")

            if counter % 2 == 0:
                og = data
                data = request_handler(data)
                write_to_file_c(og, data)
            else:
                write_to_file(data)

            counter += 1

            #data = connection.recvmsg(4096)[0]#65535
            if not data:
                break

            buffer += data
    except Exception as e:
        print('error ', e)
        pass

    return buffer


def request_handler(buffer):
    test = buffer
    case = rad.fuzz(test)#.encode("UTF-8"))
    #decodedCase = case.decode("UTF-8", "ignore")
    print("***")
    print(case)
    print("<|>")

    return buffer

def response_handler(buffer):
    # perform packet modifications
    return buffer


def proxy_handler(client_socket, remote_host, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    # counter = 1

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print("[<==] Received %d bytes from local." % len(local_buffer))
            hexdump(local_buffer)

            # if counter % 2 == 0:
            #     og = local_buffer
            #     local_buffer = request_handler(local_buffer)
            #     write_to_file_c(og, local_buffer)
            # else:
            #     write_to_file(local_buffer)
            
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")

            # counter += 1

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote." % len(remote_buffer))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[==>] Sent to local.")

        # if not len(local_buffer) or not len(remote_buffer):
        #     client_socket.close()
        #     remote_socket.close()
        #     print("[*] No more data. Closing connections.")
        #     break


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
