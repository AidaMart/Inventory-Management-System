from sqlalchemy.orm import Session
from .schema import engine, User, Contact, Base

def insert_sample_data():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Create a SessionLocal instance
    db = Session(bind=engine)

    try:
        # Sample users
        admin_user = User(username="admin", password="adminpassword")
        user1 = User(username="user1", password="user1password")

        # Add users to the session
        db.add_all([admin_user, user1])
        db.commit()

        # Sample contacts with user associations
        contact1 = Contact(name="Caroline", surname="Doe", phone="123-456-7890", email="john.doe@example.com", address="123 Main St", user=admin_user)
        contact2 = Contact(name="Jane", surname="Smith", phone="987-654-3210", email="jane.smith@example.com", address="456 Oak St", user=user1)

        # Add contacts to the session
        db.add_all([contact1, contact2])

        # Commit the changes
        db.commit()
        print("Sample data inserted successfully!")

    except Exception as e:
        print(f"Error inserting sample data: {e}")
        # Rollback in case of an error
        db.rollback()

    finally:
        # Close the session
        db.close()

# Run the insertion function when this script is executed
if __name__ == "__main__":
    insert_sample_data()
