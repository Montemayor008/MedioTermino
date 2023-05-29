from flask import Flask, render_template
import json
import grpc
import coordinates_pb2
import coordinates_pb2_grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__,template_folder='templates')

# Obtener coordenadas del servidor
def get_coords():
    channel = grpc.insecure_channel('localhost:50017/coords')
    stub = coordinates_pb2_grpc.CoordsCommStub(channel)
    
    # Realizar la llamada al servidor gRPC
    response = stub.GetCoords(coordinates_pb2.Empty())

    return response

# Flask que llama al servidor gRPC
@app.route('/call-go-api')
def call_go_api():
    coords = json.loads(MessageToJson(get_coords()))
    return render_template('home.html', coords=coords)
    
    
    

if __name__ == '__main__':
    app.run()
