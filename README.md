# AnimalShelter_CRUD_Dash_App
About the Project/Project Title
The advent of cloud computing has enabled businesses to create, store, update, and retrieve information from different geographical locations. Similarly, this program provides the user with functionality to create a document and read single or multiple documents in a distributed web application. 

I am the newest member at Global Rain, a software engineering company that specializes in making idea become reality. I was recently assigned to collaborate with innovative international rescue-animal training company. The company’s name was Grazioso Salvare. The company identifies dogs that are a good candidate for search-and-rescue.

Special attention was needed regarding the breeds of dos that were proficient in a particular area. Example: a breed may be better at water rescue. We had an opportunity to work with a common data set available to the public. It can be found be search for the animal shelter csv.

We were contracted for a full stack development application, purpose-built database, and a client-facing web application. Additionally, the client wanted the interface to be user-friendly and intuitive. Great effort was made to ensure that we were able to find specific animals that will help to rescue humans or animals that were often in life-threatening conditions.

Motivation
Secure development practices (SecDevOps) seek to reduce the common vulnerabilities and exposures associated with data transfers. While we cannot guarantee a full proof security system, there are many steps we can take to ensure data governance, data integrity, and data privacy.

This program aims to implement a 256 bit secure hash algorithm and authentication to verify the user. User privileges were assigned to regulate access to specific databases. The current program provides functionality for the user to login to the mongo database with their credentials. Afterwards, the user has access to two different functionalities. The user can create a document and/or read multiple documents.

Getting Started
Success when setting up a local environment will depend on where the database is located and your anti-virus. This program was ran using a Jupyter Notebook and Python file. If needed, pip install Pymongo in your Python environment. Create a new folder and copy and paste the program files into the folder. Note the location.

In Jupyter Notebook, click on File-Open File and find the location of the notebook file. Open the file. If the Python file is located in the same working directory, then the import statement should not display an error. Run each cell. If the import and object instantiate cells work, then the program should perform at an acceptable level for the user.

Installation
The tools needed to use the software include a computer with at least 4GB of RAM, common peripherals, supported operating system, and an internet connection. It is recommended to use Jupyter Notebooks for the integrated development environment. Instructions for downloading Jupyter Notebooks can be found here. The current program was developed and ran in a Windows 64bit environment.

Python is an open dynamically typed high level coding programming language. It is built on the DRY principle (do not repeat yourself). The application require an IDE and the download pymongo.

Import pprint only if needed. Mongo Client is a Pymongo built-in class member method used to establish a connection and access a database using the supplied parameters. Similarly, the ObjectId method can be used to find a document using a unique ID. The user will have to edit the Animal Shelter class member variables in the Python file to reflect their individual credentials.

Special consideration should be given to the username, password, database, and collection. The Mongo API is case sensitive and typos are not tolerated. Edit the data variables in the notebook file with values in dictionary format and run the program.

Code Example

Below is the Animal Shelter member method to create a document in a database. The model creates a connection and assigns values to member variables. The method checks if the data is null. When true, a PYmongo class member function is used to insert the data into the collection. When false, the method implements exception handling and displays output to the user.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/dc60cfcf-5a3a-4181-91eb-1ea775c84be4)

Tests
White box testing was conducted to ensure proper functionality. The below code shows the variable data being initialized as a dictionary and assigned a key/value pair. When the Animal Shelter object is instantiated, the connection is established and the member variables are assigned to their respective databases. A query was executed to read all the documents of animals who have the name Bella.
![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/fc453a45-35c7-4e16-9b9c-3e8a89cea6c0)

More documents that matched the criteria were generated. Above, the output shows an animal with the name Bella.

Screenshots
Below is an image showing more of the output generated from the read method.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/0f5c1774-c408-436a-95d7-e74711f71088)

Below is an output demonstrating the Animal Shelter create method and a search for the recently created document using the read method.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/d5009354-add9-4356-a1d3-a2e95d48579c)

As mentioned earlier, the client wanted their company logo displayed on the dashboard. Below is a picture showing satisfactory completion.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/e981b153-eba6-4998-93b4-fc3f1a1a6153)

Reset (returns all widgets to their original, unfiltered state)

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/e19157c2-ca17-4839-aa2c-3b82b1147ed0)

Mountain or Wilderness Rescue

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/fb1c91cf-840a-48d6-9278-7da667e47a71)

Disaster or Individual Tracking

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/2a1b97fc-e1f2-4c87-a573-d0eecb8a90e9)

Reset (returns all widgets to their original, unfiltered state)

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/7d8a6a5a-9c55-47fe-98df-02c2d48e06fa)

I would like to give a special thanks to my instructor. He guided me in the direction that I needed to go without just giving me the answer.
He is referred to in the code as Archimedes.









