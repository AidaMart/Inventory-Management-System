To get started, run

python -m address_book.db.schema  to create the schema

python -m address_book.db.sample_data_insertion to insert sample data into categories table

python -m address_book.app to run the api


To check the db follow the link https://inloop.github.io/sqlite-viewer/

To search a contact, use Postman or open terminal and 
use the following curl command to send a POST request to the /app/search endpoint:

curl -X POST -H "Content-Type: application/json" -d '{"name": "Caroline"}' http://127.0.0.1:5000/app/search
