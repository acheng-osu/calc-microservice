import logging

import grpc
import calc_pb2
import calc_pb2_grpc



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calc_pb2_grpc.CalculatorStub(channel)
        calc_string = input("Please input your string you would like to calculate: ")
        sendable_string = calc_pb2.calculateStringInput(str=calc_string)
        print("request is being made to the Calculator Microservice with the input parameter: " + calc_string)
        print("data returned by the Calculator Microservice: " + str(stub.CalculateString(sendable_string)))


if __name__ == '__main__':
    logging.basicConfig()
    run()