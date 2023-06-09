from __future__ import print_function

import logging

import grpc
import coordinates_pb2
import coordinates_pb2_grpc

# Receives coordinates from server 
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50016') as channel:
        stub = coordinates_pb2_grpc.CoordsCommStub(channel)
        response = stub.GetCoords(coordinates_pb2.Empty())
        print("Coordinates received: " + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
