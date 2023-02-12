import logging
from concurrent import futures

import calc_pb2_grpc
import grpc
import calc_pb2
import sympy


class CalculatorServicer(calc_pb2_grpc.CalculatorServicer):

    def CalculateString(self, request, context):

        calc_result = sympy.sympify(request.str)
        return calc_pb2.calculateStringOutput(result=calc_result)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  calc_pb2_grpc.add_CalculatorServicer_to_server(
      CalculatorServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()