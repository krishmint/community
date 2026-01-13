import json
from google.cloud import firestore

# Initialize Firestore client


def main(request):  # Entrypoint will be "main"
    db = firestore.Client(database="employedb")
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }


        
    try:
        # Parse incoming JSON
        request_json = request.get_json(silent=True)
        if not request_json:
            return ("Invalid or missing JSON body", 400, headers)

        employee_id = request_json.get('employeeId')

        if not employee_id:
            return ("Missing 'employeeId'", 400, headers)

        # Reference to document
        doc_ref = db.collection("EmployeeDB").document(employee_id)

        # Delete document
        doc_ref.delete()

        return (json.dumps({'message': f"Employee with ID {employee_id} deleted successfully"}), 200, headers)

    except Exception as e:
        return (json.dumps({"error": str(e)}), 500, headers)
