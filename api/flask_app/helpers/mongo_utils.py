from api.flask_app.helpers.db_helper import ASC_SORT_ORDER, get_database
import pymongo


class MongoClass:
    def __init__(self, db_name):
        self.db = get_database(db_name)
        self.db = self.db[db_name]

    def get_collection(self, collection_name):
        collection = self.db[collection_name]
        return collection

    def insert_document(self, collection, document):
        # Insert a document into the collection
        inserted_document = collection.insert_one(document)
        return inserted_document.inserted_id

    def find_documents(self, collection, query, projection={}, sortKey=False, sortOrder=pymongo.ASCENDING):
        # Query documents in the collection
        if sortKey:
            results = collection.find(
                query, projection).sort(sortKey, sortOrder)
        else:
            results = collection.find(query, projection)
        return list(results)

    def find_one_document(self, collection, query, projection={}):
        # Query documents in the collection
        results = collection.find_one(query, projection)
        return results

    def update_many_document(self, collection, query, update_data):
        # Update a document in the collection
        update_result = collection.update_many(
            query, {'$set': update_data})
        return update_result.modified_count
    
    def find_one_and_update(self, collection, query, update_data, upsert=False):
        # Update a single document in the collection and return the updated document
        updated_document = collection.find_one_and_update(
            query,
            update_data,
            return_document=pymongo.ReturnDocument.AFTER,  # To return the updated document
            upsert=upsert
        )
        return updated_document
    


    def delete_documents(self, collection, query):
        # Delete documents from the collection
        delete_result = collection.delete_many(query)
        return delete_result.deleted_count

    def aggregate_documents(self, collection, match, group):
        # Aggregate documents in the collection
        results = collection.aggregate([{"$match": match}, {"$group": group}])
        return results
