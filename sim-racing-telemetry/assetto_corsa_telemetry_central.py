"""
Script for sending Assetto Corsa UDP data to Arduino via Serial communication
"""

import socket
import struct
import serial


# assetto corsa UDP stuff
ip = '127.0.0.1' # localhost ip
udp_port = 9996  # udp port

# arduino serial port stuff
controller_port = 'COM81'
controller_bdrate = 115200

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

identifier = 1
version = 1
operationId = 0

handshaker = struct.pack('iii', 1, 1, 3)

client_socket.sendto(handshaker, (ip, udp_port))


try:
    handshaker = struct.pack('iii', identifier, version, operationId)

    client_socket.sendto(handshaker, (ip, udp_port))
    print("\n\n 1. Client Sent : ", struct.unpack('iii', handshaker), "\n\n")
    data, address = client_socket.recvfrom(4096)
    for x in data:
        print(chr(x), end="")
    print()
    result = struct.unpack('100s100sii100s100s', data)

    handshaker = struct.pack('iii', 1, 1, 1)
    client_socket.sendto(handshaker, (ip, udp_port))

    while True:
        data, address = client_socket.recvfrom(4096)
        result = struct.unpack(
            'cifff??????xfffiiiifffffiffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', data)

        # car_rpm = result[21]                  # float
        # car_gear = result[23]-1               # int
        # car_gas = round(result[18], 1)        # float
        # car_brake = round(result[19], 1)      # float

        data = struct.pack('fiff', result[21], result[23]-1, round(result[18], 1), round(result[19], 1))
        print(data)

        ## send struct to arduino
        # print("rpm: ", car_rpm, "gear: ", car_gear, "gas: ", car_gas, "brake: ", car_brake)

except Exception as e:
    print(e)
    handshaker = struct.pack('iii', 1, 1, 3)
    client_socket.sendto(handshaker, (ip, udp_port))
