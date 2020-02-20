Instructions: 
	- Consume the config.json file on your REST Server
	- Create storage directory for nodes as per the config file. Ex. uploads should be the name of the directory that contains the nodes
	- Nodes must be named as node_<node_number> . eg. node_1 , node_2..
	- Use the Postmancollection.json file for the collection of requests . Create your server to work with the given template of requests
	- Alternatively, the requests collections can be downloaded @ https://www.getpostman.com/collections/76e732538fe48439bfc2
	- Postman -> import -> from Link . to import a collection
	- Configure your server to reset on restart. 
	- Do not add a trailing "/" after your endpoint

RUN TESTS: 
	- use the following command to run the tests ( without "<>" ofcourse! ) 

	runvalidation.exe -e <your server detail> -t sanity -r <your roll number> 


Sanity: 
		runvalidation.exe -e <your server detail> -t sanity -r <your roll number> 

Milestone1: 
		runvalidation.exe -e <your server detail> -t milestone1 -r <your roll number> 	

Milestone1B:
		runvalidation.exe -e <your server detail> -t milestone1b -r <your roll number> 

Milestone3: 
		runvalidation.exe -e <your server detail> -t milestone3 -r <your roll number> 