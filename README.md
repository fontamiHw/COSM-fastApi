
# COSM-fastap
A web-ui application to debug the webex bot

     


## Prerequisite
 1. Python 3.10 or above
 2. the following python library:
     - "fastapi[standard]"==0.115.6    
     - python-multipart==0.0.19
  3. The log files will be write in a specific path that sahll be present
      on the disk three directory are required and this shall be theire name
        - logs
        - files 
        - resources

     


## Configuration file
The app use the `CosmFastapi-config` file to change its beaviour.
The first run of the app in any of the 2 modes will copy the default file in the `resources` directory and use that.
Any other runs does not overwrite the config file.
There are 2 ways to start then:

 1. Run the app, stop it, change the config, run again
 2. Copy the `CosmFastapi-config` under the `resources` directory, edit and run

Any element is described in the yaml file itself
     


## Local Mode
###  setUp
 1. Create the three directories described before and update that in the
    `start.sh` script    
    >     NOTE: It is not importand where they are located.
    >     They could be in different mount of the disk but is important that 
    >          the path is correctly written in the above script    
 
###  Run
Simply run the script `start.sh` 

     


## Docker Mode
###  setUp
 - ***Network***
It is required a Newtork bridge for the internal communication between the 2 containers that compose the whole tool.
The network must be the same as the other container  ([COSM-webex](https://wwwin-github.cisco.com/mfontane/COSM-webex)) it is working with.
 - ***Host volume***
 The Host shall have the three directories described above already presents on disk.
 All the three directories **must be under the same root directory**
 write the path in the  ***HOST*** variable within the  `Docker/startCosmBoth.sh` script
 - ***network***
docker network create --driver=bridge --subnet=172.20.0.0/24 --gateway 172.20.0.1 Cosm-net

  

### Run
Simply run the `Docker/startCosmBoth.sh` script

     


## Docker Creation
Adapt the script `Docker/createImage.sh` at your need (maybe the name of the image)
Simply run the script 

