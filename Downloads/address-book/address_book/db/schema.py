from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Define the database connection URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    # Add the back-reference to the Contact table
    contacts = relationship('Contact', back_populates='user')

# Define the Contact model
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(120), nullable=False)
    address = Column(String(200), nullable=False)

    # Add foreign key relationship to the User table
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='contacts')

# Create the tables in the database
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
