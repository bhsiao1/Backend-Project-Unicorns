# Backend Project

Tech stack:
Flask and Python with MongoDB as the database system.

Theme: Unicorns
Each unicorn has a data schema of 5 fields: name, fur, hornLength, isBaby, and owner.
Each ride has a data schema of 3 fields: user, unicorn, duration.

This project consists of backend API endpoints that allow us to post or get certain unicorns as well as ride a unicorn and get the longest rider for a unicorn.

/unicorns:
POST => inserts a unicorn into the MongoDB database.
GET => fetches all unicorns in the database.

/ride:
POST => inserts a ride into the MongoDB database.

/longest_rider/<unicorn_id>:
GET => fetches the ride with the longest duration for the ride that has the matching unicorn ID. if none, returns error.

