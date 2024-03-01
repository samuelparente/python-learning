# Samuel Parente
# Platform for manage clients
# Learning purposes
# Python and MongoDB

# System "things"
import sys
import json
from prettytable import PrettyTable
from bson import ObjectId
# MongoDB drivers
import pymongo

# credentials
username = "samuelparente"
password = "wj7wANkmsakBtaGM"

# Database
database = "db_test"
myCollection = "clientsDB"
uri = 'mongodb+srv://samuelparente:' + password + '@cluster0.zov42uq.mongodb.net/?retryWrites=true&w=majority&appName='+ database

# -------------------------- JSON FOR TESTING --------------------------------------------
exampleClients = [
                    {
                        "first_name": "Michael",
                        "last_name": "Johnson",
                        "country": "USA",
                        "email": "michael.johnson@example.com"
                    },
                    {
                        "first_name": "Sophia",
                        "last_name": "Moore",
                        "country": "Canada",
                        "email": "sophia.moore@hotmail.com"
                    },
                    {
                        "first_name": "Ava",
                        "last_name": "Smith",
                        "country": "UK",
                        "email": "ava.smith@yahoo.com"
                    },
                    {
                        "first_name": "Alexander",
                        "last_name": "Wilson",
                        "country": "Australia",
                        "email": "alexander.wilson@gmail.com"
                    },
                    {
                        "first_name": "William",
                        "last_name": "Miller",
                        "country": "Germany",
                        "email": "william.miller@example.com"
                    },
                    {
                        "first_name": "Sophia",
                        "last_name": "Williams",
                        "country": "France",
                        "email": "sophia.williams@hotmail.com"
                    },
                    {
                        "first_name": "Emma",
                        "last_name": "Taylor",
                        "country": "Japan",
                        "email": "emma.taylor@example.com"
                    },
                    {
                        "first_name": "Olivia",
                        "last_name": "Johnson",
                        "country": "China",
                        "email": "olivia.johnson@hotmail.com"
                    },
                    {
                        "first_name": "Isabella",
                        "last_name": "Wilson",
                        "country": "India",
                        "email": "isabella.wilson@example.com"
                    },
                    {
                        "first_name": "Michael",
                        "last_name": "Davis",
                        "country": "Brazil",
                        "email": "michael.davis@example.com"
                    },
                    {
                        "first_name": "Emma",
                        "last_name": "Johnson",
                        "country": "USA",
                        "email": "emma.johnson@hotmail.com"
                    },
                    {
                        "first_name": "James",
                        "last_name": "Brown",
                        "country": "Canada",
                        "email": "james.brown@gmail.com"
                    },
                    {
                        "first_name": "Ava",
                        "last_name": "Wilson",
                        "country": "UK",
                        "email": "ava.wilson@hotmail.com"
                    },
                    {
                        "first_name": "Alexander",
                        "last_name": "Moore",
                        "country": "Australia",
                        "email": "alexander.moore@example.com"
                    },
                    {
                        "first_name": "Sophia",
                        "last_name": "Miller",
                        "country": "Germany",
                        "email": "sophia.miller@hotmail.com"
                    },
                    {
                        "first_name": "Olivia",
                        "last_name": "Davis",
                        "country": "France",
                        "email": "olivia.davis@example.com"
                    },
                    {
                        "first_name": "James",
                        "last_name": "Williams",
                        "country": "Japan",
                        "email": "james.williams@example.com"
                    },
                    {
                        "first_name": "William",
                        "last_name": "Taylor",
                        "country": "China",
                        "email": "william.taylor@hotmail.com"
                    },
                    {
                        "first_name": "Isabella",
                        "last_name": "Brown",
                        "country": "India",
                        "email": "isabella.brown@example.com"
                    },
                    {
                        "first_name": "John",
                        "last_name": "Smith",
                        "country": "Brazil",
                        "email": "john.smith@example.com"
                    }
                ]

# ----------------------------------------------------------------------------------------

# Function to show main menu
def showMainMenu():
    print ("\n********** CLIENTS DATABASE MONGODB **********\n")
    print ("1 - Search client")
    print ("2 - Add client")
    print ("3 - Modify client")
    print ("4 - Delete client")
    print ("5 - List all clients")
    print ("6 - Exit\n")


# Function to show update client menu
def showMenuUpdateClient():
    print ("1 - Name")
    print ("2 - Lastname")
    print ("3 - Country")
    print ("4 - email")
    print ("5 - Back")
    print ("Select field to update: ")

#Function to read input for a new client
def readClientInput():
    # Prompt the user to enter client information in a single line
    print("\nEnter client information (comma-separated)")
    input_str = input("Format: firstname,lastname,country,email: ")

    # Split the input string based on comma (,) delimiter
    input_list = input_str.split(',')

    # Check if the input is in the correct format
    if len(input_list) != 4:
        print("\nInvalid input format. Please enter all fields separated by commas.\n")
        return None

    # Extract client information from the input list
    firstname, lastname, country, email = input_list

    # Return the client information as a dictionary
    client_info = {
        "first_name": firstname.strip(),
        "last_name": lastname.strip(),
        "country": country.strip(),
        "email": email.strip()
    }
    return client_info


# Function to show records
def showRecord(records):
    if records:
        table = PrettyTable()
        table.field_names = ["Id", "First Name", "Last Name", "Country", "Email"]
        for record in records:
            table.add_row([record["_id"],record["first_name"], record["last_name"], record["country"], record["email"]])
        print(table)
    else:
        print("No records found.")


# Function to search client
def searchClient(collectionInUse, query):
      
    # Perform a query to find records matching the search criteria
    results = collectionInUse.find({"$or": [{"first_name": {"$regex": query, "$options": "i"}},
                                          {"last_name": {"$regex": query, "$options": "i"}},
                                          {"country": {"$regex": query, "$options": "i"}},
                                          {"email": {"$regex": query, "$options": "i"}}]})
    return results


# Function to delete client
def deleteClient(collectionInUse, client_id):
    # Convert client_id to ObjectId
    try:
        client_id = ObjectId(client_id)
    except Exception as e:
        print("Invalid ObjectId format:", e)
        return

    # Ask for confirmation before proceeding with delete operation
    confirmation = input("\nWARNING: This will permanently delete the record. Do you want to continue? (yes/no): ")
    if confirmation.lower() != "yes":
        print("Operation cancelled.")
        return

    # Perform delete operation based on ObjectId
    result = collectionInUse.delete_one({"_id": client_id})
    
    # Check if the delete operation was successful
    if result.deleted_count == 1:
        print("Client with ID ", client_id, " deleted successfully.\n")
    else:
        print("No client found with ID ", client_id)


# Function to insert new client
def insertClient(collectionInUse, new_client):
    result = collectionInUse.insert_one(new_client)
    print("\nNew client inserted with ID:", result.inserted_id + "\n")


def updateClient(collectionInUse, client_id):
    # Convert client_id to ObjectId
    try:
        client_id = ObjectId(client_id)
    except Exception as e:
        print("Invalid ObjectId format:", e)
        return

    # Prompt the user to select the field to update
    field_to_update = promptForUpdateField()

    # Prompt the user for the new value
    new_value = input("Enter the new value for {}: ".format(field_to_update))

    # Perform update operation based on the selected field
    update_field = None
    if field_to_update.lower() == "firstname":
        update_field = "first_name"
    elif field_to_update.lower() == "lastname":
        update_field = "last_name"
    elif field_to_update.lower() == "country":
        update_field = "country"
    elif field_to_update.lower() == "email":
        update_field = "email"
    else:
        print("Invalid field to update:", field_to_update)
        return

    # Update the selected field in the document
    result = collectionInUse.update_one({"_id": client_id}, {"$set": {update_field: new_value}})
    
    # Check if the update operation was successful
    if result.modified_count == 1:
        print("Client with ID", client_id, "updated successfully.")
    else:
        print("No client found with ID", client_id)


# Function to prompt the user to select a field to update
def promptForUpdateField():
    # Prompt the user to select a field to update
    print("Which field do you want to update?")
    print("1. First name")
    print("2. Last name")
    print("3. Country")
    print("4. Email")
    choice = input("Enter the number corresponding to the field you want to update: ")
    
    # Map user's choice to the corresponding field
    fields = {"1": "firstname", "2": "lastname", "3": "country", "4": "email"}
    return fields.get(choice)


# Function to retrieve all the records
def retrieveAllRecords(collectionInUse):
 
    all_records = collectionInUse.find()
    return all_records


# Function to connect to database mongoDB
def connectToDB(uri):
    
    # Try to connect
    try:
        clientCon = pymongo.MongoClient(uri)
        return clientCon
    except pymongo.errors.ConfigurationError:
        print("Error connectiong to mongoDB.")
        sys.exit(1)


# Function to close the connection to the database mongoDB
def closeConToDB(clientCon):
    clientCon.close()


# Function to create a collection
def createCollection(clientCon, database ,collection):
    db = clientCon.database
    collectionInUse = db.create_collection(collection)
    return collectionInUse


# ------------------------- MAIN PROGRAM -------------------------

# Connect
clientCon = connectToDB(uri)
#print(client)

# Create collection
#collectionInUse = createCollection(clientCon,database,myCollection)

#Select db and collection
db = clientCon[database]
collectionInUse = db[myCollection]

# Insert data (debug - 20 clients list)
#collectionInUse.insert_many(exampleClients)

while(1):
    # Show menu
    showMainMenu()

    # Read option
    opt_user = input("Select option:")

    try:
        opt = int(opt_user)

        if opt == 1:
           user_query = input("Enter what are you looking for:").strip()
           recordFound = searchClient(collectionInUse,user_query)
           showRecord(recordFound)
        elif opt == 2:
            user_input = readClientInput().strip()
            insertClient(collectionInUse, user_input)
        elif opt == 3:
            update_field = promptForUpdateField()
            client_id = input("Enter the client ID: ").strip()
            updateClient(collectionInUse, client_id, update_field)
        elif opt == 4:
            id_input = input("Enter the id of the client to delete:").strip()
            deleteClient(collectionInUse, id_input)
        elif opt == 5:
            allRecords = retrieveAllRecords(collectionInUse)
            showRecord(allRecords)
        elif opt == 6:
            print("\nGoodbye.\n")
            break
        else:
            print ("\nNot a valid option.\n")
    except:
        print("\nInvalid input. Please enter a number.\n")

# Close
closeConToDB(clientCon)
