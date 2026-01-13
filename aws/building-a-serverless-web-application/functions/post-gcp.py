import json
from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client(database="employedb")

def main(request):   # entrypoint name = "main"
    
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
         }
    
    try:
        
        # Parse incoming JSON
        request_json = request.get_json(silent=True)

        if not request_json:
            return ("Invalid or missing JSON body", 400)

        name = request_json.get('name')
        employee_id = request_json.get('employeeId')
        email = request_json.get('email')
        address = request_json.get('address')
        phone = request_json.get('phone')

        if not employee_id:
            return ("Missing 'employeeId'", 400)

        # Reference to collection and document
        doc_ref = db.collection("EmployeeDB").document(employee_id)

        # Save to Firestore
        doc_ref.set({
            'employeeId': employee_id,
            'name': name,
            'email': email,
            'address': address,
            'phone': phone
        })

        return (json.dumps({"message": "Employee inserted successfully"}), 200, headers)

    except Exception as e:
        return (json.dumps({"error": str(e)}), 500)
