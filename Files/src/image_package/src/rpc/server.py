#!/usr/bin/env python3
from concurrent import futures
import logging
import sys
import time
import signal
import grpc
import coordinates_pb2
import coordinates_pb2_grpc
import rospy
from geometry_msgs.msg import PointStamped



class Comm(coordinates_pb2_grpc.CoordsCommServicer):
    def __init__(self):
        self.coords = PointStamped()
        rospy.Subscriber("object_topic", PointStamped, self.coord_callback)
    def GetCoords(self, request, context):
        return coordinates_pb2.PointStamped(
          
            point=coordinates_pb2.PointStamped.Point(
                x=self.coords.point.x,
                y=self.coords.point.y,
                z=0,
                seq=self.coords.header.seq,
                stamp=int(self.coords.header.stamp.to_sec()),
                frame_id=self.coords.header.frame_id
            )
        )
    def coord_callback(self,data):
        self.coords = data

def terminate_server(signum, frame):
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')

    # do whatever...
    time.sleep(1)
    sys.exit(0)





def serve():
    port = '50016'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coordinates_pb2_grpc.add_CoordsCommServicer_to_server(Comm(), server)
    
    
    server.add_insecure_port('127.0.0.1:' + port)
    server.start()
    print("Server started, listening on " + port)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped.")

    
if __name__ == '__main__':
    signal.signal(signal.SIGINT, terminate_server)
    rospy.init_node('grpc_server', anonymous=True)
    logging.basicConfig()
    serve()
