# AnimalShelter_CRUD_Dash_App
About the Project/Project Title
The advent of cloud computing has enabled businesses to create, store, update, and retrieve information from different geographical locations. Similarly, this program provides the user with functionality to create a document and read single or multiple documents in a distributed web application. 

Motivation
Secure development practices (SecDevOps) seek to reduce the common vulnerabilities and exposures associated with data transfers. While we cannot guarantee a full proof security system, there are many steps we can take to ensure data governance, data integrity, and data privacy.

This program aims to implement a 256 bit secure hash algorithm and authentication to verify the user. User privileges were assigned to regulate access to specific databases. The current program provides functionality for the user to login to the mongo database with their credentials. Afterwards, the user has access to two different functionalities. The user can create a document and/or read multiple documents.

Getting Started
Success when setting up a local environment will depend on where the database is located and your anti-virus. This program was ran using a Jupyter Notebook and Python file. If needed, pip install Pymongo in your Python environment. Create a new folder and copy and paste the program files into the folder. Note the location.

In Jupyter Notebook, click on File-Open File and find the location of the notebook file. Open the file. If the Python file is located in the same working directory, then the import statement should not display an error. Run each cell. If the import and object instantiate cells work, then the program should perform at an acceptable level for the user.

Installation
The tools needed to use the software include a computer with at least 4GB of RAM, common peripherals, supported operating system, and an internet connection. It is recommended to use Jupyter Notebooks for the integrated development environment. Instructions for downloading Jupyter Notebooks can be found here: https://www.partitionwizard.com/partitionmanager/how-to-install-jupyter-notebook.html. The current program was developed and ran in a Windows 64bit environment.

Import pprint only if needed. Mongo Client is a Pymongo built-in class member method used to establish a connection and access a database using the supplied parameters. Similarly, the ObjectId method can be used to find a document using a unique ID. The user will have to edit the Animal Shelter class member variables in the Python file to reflect their individual credentials.

Special consideration should be given to the username, password, database, and collection. The Mongo API is case sensitive and typos are not tolerated. Edit the data variables in the notebook file with values in dictionary format and run the program.

Code Example

Below is the Animal Shelter member method to create a document in a database. The model creates a connection and assigns values to member variables. The method checks if the data is null. When true, a PYmongo class member function is used to insert the data into the collection. When false, the method implements exception handling and displays output to the user.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/f60bbcf6-a2a8-4436-85b3-044f3719cded)

Upload the Austin Animal Center Outcomes data set into MongoDB

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/9c40bed7-bae5-41ee-bbc2-e5a300772eb7)

The Grazioso Salvare project requires the animal shelter csv to be imported into the proper location. The above image shows the query and how many documents were successfully imported.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/2222192e-2028-4bb3-9f12-fb8ae7a0c7fd)

The above shows a query to generate the current databases. The project requires the animal shelter csv to be imported as the AAC database. Satisfaction of this requirement is reflected above.

Create a user account in the mongo shell to ensure user authentication to the database and collection.

Special attention should be given to the authentication database, user access credentials/privileges, and port number. A query was executed to create a user in the admin database. Instructions mention to authenticate the root user in the admin database and add users in the test database. I could not login as a user when I authenticated the user in the test database. I had to create the user in the admin database. Below is an image showing the user logging in and the connection status.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/273efd30-e88a-4db5-8b4b-b10a6967e86f)

The above shows the user’s login name and password. A shell command was written to output the user’s login credentials. The user is able to log into mongo shell and their roles are shown in the output.

Develop a CRUD Python module in a PY file and import your Python code

Read: White box testing was conducted to ensure proper functionality. The below code shows the variable data being initialized as a dictionary and assigned a key/value pair.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/77f963bf-4df0-421e-bcb1-41c29b01b65c)

When the Animal Shelter object is instantiated, the connection is established and the member variables are assigned to their respective databases. A query was executed to read all the documents of animals who have the name Bella.
Create: The client would like for the user to have the ability to create a new document and add it to the database. Additionally, the program should return ‘True’ after the request has been performed. The query below uses the object that was instantiated earlier. A new document is passed as an argument to the Animal Shelter member method create. 

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/f3014277-fe20-4079-817e-9e1cedd48958)

The return value from the function call, displayed above, is true. For continuity, another query was executed to output the new document that was created.
Update: Information changes on a regular basis. The client needed the ability to update the documents in the database. The same object instantiation was used to call a member function to update a document. The method is passed a new document in dictionary format. Below are the test statements.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/d9aa4964-b89a-4d41-b05e-322faa811775)

Referencing the above, a function call to db.read is passed an argument and the return values are outputted in the images. A variable is declared and initialized with a new document in dictionary format. The search document parameters are saved as a variable. A function call to the update member method returns the number of matching documents. The return value above is 1.
For continuity, another call to db.read was made to verify the recent change. The update is reflected in the image above.
Delete: Sometimes information has to be deleted when it is no longer relevant or needed. The client wanted the program to delete specific documents in the database. The program implements a function that takes a document as an argument and searches for the document. If a document is found, then the method deletes the document and return the number of documents deleted.
![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/d038c9ab-c794-4e4b-9166-5b13a9646832)

Following the same structure as the previous method, the delete function returns an integer assigned to the Delete Result deleted count value. One match was found and deleted.

Company Logo

As mentioned earlier, the client wanted their company logo displayed on the dashboard. Below is a picture showing satisfactory completion.

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/b040ffac-4984-4ecc-a093-c6a62a7ad980)

Reset (returns all widgets to their original, unfiltered state)

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/d381fa24-3475-4356-aea6-3ff5afc8e506)

Mountain or Wilderness Rescue

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/0ea70002-0075-479e-9e53-b14ccfd64d9a)

Disaster or Individual Tracking

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/678d5e51-e2d4-453e-89c3-5557939ec0d0)

Water Rescue

![image](https://github.com/mwesley8/AnimalShelter_CRUD_Dash_App/assets/105822088/67951155-c0e9-4de6-a4ad-dfb1ecf7917a)

Special thanks to my instuctor. We collaborated together to produce the best possible dashboard relative to my level of understanding.
The biggest lessong I learned was that it is okay to ask for help.

Maurice Wesley








