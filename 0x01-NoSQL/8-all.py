def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object

    Returns:
        A list of all documents in the collection. If no documents are found, returns an empty list.
    """
    # Count documents
    document_count = mongo_collection.count_documents({})
    if document_count == 0:
        return []
    
    # Retrieve all documents and convert the cursor to a list
    return list(mongo_collection.find())

