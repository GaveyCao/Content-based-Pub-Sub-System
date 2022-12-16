# Content-based-Pub-Sub-System
##Requirements:
###-PyMongo
    python3 -m pip install pymongo
###-gRPC
    python -m pip install grpcio
    python -m pip install grpcio-tools
###-MongoDB
You can install local mongdb database, or sign up the mongdb Atlas to get a free cluster, and replace connection string with your own one.
###-AWS EC2
Sign up a AWS account and start free instances for deployment. Change IP address to localhost to run locally
###Setting Up:
####1: Install and register all the requirements
####2: Generate gRPC protocol buffer if necessary: 
    python -m grpc_tools.protoc -I proto/ --python_out=.--grpc_python_out=. Pr.proto 
####3: Start the project in the following order:
    python3 central_server.py
    python3 backup_server.py
    python3 virtual_server.py
    python3 frontend.py 50049 (or any free port) python3 client.py 50048 (or any free port) 
####4: Start more frontend and client if you like
####5: Follow the instructions to use the pub-sub system
