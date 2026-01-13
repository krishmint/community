import json
from google.cloud import firestore
from flask import jsonify

# Initialize Firestore client


def main(request):

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if request.method == "OPTIONS":
        return ("", 204, headers)

    db = firestore.Client(database="employedb")
    
    try:
        # Get all documents from Firestore collection
        docs = db.collection("EmployeeDB").stream()

        data = []
        for doc in docs:
            item = doc.to_dict()
            item['id'] = doc.id  # optional: include document ID
            data.append(item)

        return (jsonify(data), 200, headers)

    except Exception as e:
        return (json.dumps({"error": str(e)}), 500, headers)


