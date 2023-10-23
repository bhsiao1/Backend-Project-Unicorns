**Design Doc**
Why did you choose to organize your data schemas/models in a particular way?
Feel free to talk a bit about the "harder" routes that you worked on and how you approached them — harder is completely subjective, so feel free to get creative here!
How did you decide on certain response codes?
This should be at most a page, so feel free to be brief!


I chose to organize my data schemas in this particular way of using MongoDB in Python was because I wanted to use a language I was already familiar with (Python), so I
decided to use Flask for an easier time to read documentation and implement commands for my functions. MongoDB seemed better than NoSQL for this project because MongoDB
supports searching for queries better than NoSQL does. I just used dictionaries and strings to give the data in.

The harder routes that I worked on was definitely the start of trying to figure out how to start with implementing Flask and MongoDB. That took a lot of reading through documentations and searching up
how to start up Flask and MongoDB with imports, downloading the software, and reading basic code for initialization. That took up most of the time for almost completing the project.

Another hard route that I worked on was definitely get unicorns one, as I was not sure how to fix the errors I was getting with _iD not being able to be JSON serialized.
For this problem, I approached them by trying different ways first. First, I tried changing the type for _iD as a string. However, that would return the _iD with the
unicorns' other features. Thus, I tried searching up more specific documentation on the find function. That led me to find out about projection, which would allow me to
exclude _iD from the key/value of features. However, I was not able to figure out how to return it in the order it was registered as it returned it alphabetically.

Lastly, a very challenging route I worked on was the get longer rider function, as I was unable to figure out the logic for finding, sorting, then returning just the user of the
longest rider. I was very stumped on this, trying different ways with orders of when to use the list and sort methods, either before or after checking if the length of riders with that unicorn_d was 0.
I did lots of searching through documentation on sort and how to get a certain row and key/value pair from it. When I finally got that, I needed to figure out
what to put in my error message. I searched up what response code to put, and it turns out that 400-499 was for if the error was caused by the user vs 500-599 is for error caused by server.
Because this was a user error due to them inputting an unicorn_id that doesn't exist, I used 400 as response code.
