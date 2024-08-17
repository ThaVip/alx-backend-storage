#!/usr/bin/env python3
from pymongo import MongoClient

def get_count():
    """Return the count of documents in the collection."""
    # Create a MongoClient instance to connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    
    # Access the specific database
    db = client['logs']
    
    # Access the collection within the database
    collection = db['nginx']
    
    # Get the count of documents in the collection
    count = collection.count_documents({})
    
    # Close the connection
    client.close()
    
    return count




def count_methods():
    """Return the count of documents for each HTTP method."""
    # Create a MongoClient instance to connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Access the specific database
    db = client['logs']

    # Access the collection within the database
    collection = db['nginx']

    # Define the methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Dictionary to hold the counts for each method
    counts = {}

    # Count documents for each method
    for method in methods:
        counts[method] = collection.count_documents({"method": method})

    # Close the connection
    client.close()

    return counts



def count_one():
    """Return the count of documents for each HTTP method."""
    # Create a MongoClient instance to connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Access the specific database
    db = client['logs']

    # Access the collection within the database
    collection = db['nginx']
    

    query = { 
         
       "$and": [
            
           { "method" : "GET" },
           { "path" : "/status"}

           ] 
       } 

    final = collection.count_documents(query)

    client.close()

    return final



def main():
    """Main function to print the count of documents."""
    bad = get_count()
    print(f"{bad} logs")
    


    """Main function to print the count of documents for each HTTP method."""
    counts = count_methods()
    print("methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\t{method}: {counts[method]}")


    ready = count_one()

    print(f"{ready} status check")




if __name__ == "__main__":
    main()
