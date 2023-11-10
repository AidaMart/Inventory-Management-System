from flask import Flask, request, jsonify
from ..db import User, Contact, SessionLocal, engine, Base
from sqlalchemy import or_

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

# Route to search contacts based on JSON input
@app.route('/app/search', methods=['POST'])
def search_contacts():
    try:
        search_criteria = request.json

        if not search_criteria:
            return jsonify({'error': 'JSON input not provided'}), 400

        session = SessionLocal()

        # Create a filter based on the provided criteria
        filter_criteria = []
        for field in ['name', 'surname', 'phone', 'email', 'address']:
            if field in search_criteria:
                filter_criteria.append(or_(getattr(Contact, field).ilike(f"%{search_criteria[field]}%")))

        if not filter_criteria:
            return jsonify({'error': 'No valid search criteria provided'}), 400

        # Search contacts based on the filter criteria
        contacts = session.query(Contact).filter(*filter_criteria).all()

        contact_list = [
            {
                'id': contact.id,
                'name': contact.name,
                'surname': contact.surname,
                'phone': contact.phone,
                'email': contact.email,
                'address': contact.address,
                'user_id': contact.user_id
            }
            for contact in contacts
        ]

        return jsonify({'contacts': contact_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
