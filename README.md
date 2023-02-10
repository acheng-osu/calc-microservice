# String Calculator Microservice

## Information
This microservice allows a user to input a string representing a sequence of arithmetical calculations and obtain the result of the calculations. Our communication approach uses gRPC which is an API architectural style which will allows end users to call remote methods and services as if they were local objects. In our case, end users will pass a string parameter representing a series of calculations to our remote string calculator service via an interface resembling calling a local class method. The calculator service will then return an integer representing the result of said calculations to the end user.

## Making a connection with the microservice
### *(Preferred)* Case 1: end user clones this repository
You're all set up!

### Case 2: starting from scratch
In your project root directory, create a new directory `protos` and create a file `calc.proto` and populate it so it's identical to the `calc.proto` file in this repository

`cd` to the project root directory and run the below code to automatically generate the required code/files to make a connection.

```
python3 -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/calc.proto
```

Follow the instructions in this [guide](https://grpc.io/docs/languages/python/basics/#server) to continue setup.


### Final steps
Once you've finished set-up, all that's left is to standup the microservice and instantiate a connection to it.

#### Standing up the microservice
The code necessary to stand up the microservice can be found in the `calc_server.serve()` method. Note the port number the developer has chosen as you will need this on the client/end user side to connect to the microservice.

#### Connecting to the microservice
The code necesarry to instantiate a connection to the microservice can be found in the `calc_client.run()` method.
A few notes:
- replace "hostname" with the port number from the previous section in the `grpc.insecure_channel(hostname)` call.
- declaring the stub functionally serves as declaring a instance of the microservice on the user-end. You can use this stub to call the necessary microservice methods. We will detail the communication contract with now available below.


## How to request data
As detailed in the `calc.proto` file, there are input data we need to provide the microservice in our service request.
The `.proto` file specifies the appropriate input data type for service request. In our case, to use the `CalculateString()` service, we need to provide a `calc_pb2.calculateStringInput()` object. We will specifiy the string to calculate as a member of this object. Once we have this object, we can use it as an input parameter in the microservice method call. An example call is shown below.

```
//creating an object of type calculateStringInput
calc_string = calc_pb2.calculateStringInput(str="4+3+5-7")

//calling the microservice method
stub.CalculateString(calc_string)

```

## How to receive data
The received data will be returned by the microservice method call, just like a local method call. In our case, our microservice will perform the calculations on the string and return the integer result to the caller.

Example:
```
result = stub.CalculateString(calc_string)

print(result) //expected output: 5

print(type(result)) //expected output: <class 'int'>
```

## UML diagram