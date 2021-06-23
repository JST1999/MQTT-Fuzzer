import ipaddress
import os
import socket
import struct
import sys

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

class IP:
    def __init__(self, buff=None):
        header2 = struct.unpack('<20s', buff)
        #print(header2)

        header = struct.unpack('<BBHHHBBH4s4s', buff)
        #print(header)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF
    
        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # human readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('%s No protocol for %s' % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)

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

def sniff(host):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    if  os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65535)[0]
            print(raw_buffer)
            hexdump(raw_buffer)
            ip_header = IP(raw_buffer[0:20])
            print('Protocol: %s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
            print(f'Version: {ip_header.ver} Header Length: {ip_header.ihl}  ToS: {ip_header.tos}  TL: {ip_header.len}')
            print(f'ID: {ip_header.id} Offset: {ip_header.offset}')
            print(f'Time to Live: {ip_header.ttl} Protocol Num: {ip_header.protocol_num} Header Checksum: {ip_header.sum}')
            print()
                
    except KeyboardInterrupt:
        if  os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '192.168.0.7'
    sniff(host)
