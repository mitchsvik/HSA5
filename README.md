# HSA5
Stress Testing

### Project contains a web application that defines three routes:

- `GET /`: This route fetches all the notes from the 'notes' collection in the 'hsa5' database and returns them as a JSON response.

- `POST /`: This route creates a new note in the 'notes' collection. The note data is received as a JSON payload in the request. The current date and time is added to the note data as 'created_at' before it is inserted into the database. The ID of the inserted note is returned in the response.

- `DELETE /`: This route deletes all notes from the 'notes' collection.

The application stores data in mongoDB

### Application testing

`siege.sh` is used to simulate load on a API by creating multiple concurrent users using the `siege` tool:

1. It waits for the database to initialize by pausing the script for 15 seconds.
2. It runs a sub-script `siege-wave.sh` with a parameter - amount of concurrent users. The script simulates waves of 10, 25, 50, and 100 concurrent users.
