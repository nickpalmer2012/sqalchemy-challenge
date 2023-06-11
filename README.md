# sqalchemy-challenge
Module 10 Challenge

### How to create engine for sqlite database
- I utilized the "Chinhook_db_analysis" in class challenge file to borrow code to create the engine to link the notebook to the sqlite database.



### How to filter items between two dates in a session query:

- ![Screenshot 2023-06-09 at 4 40 04 PM](https://github.com/nickpalmer2012/sqalchemy-challenge/assets/128104435/f748ef58-fdea-42e6-9514-907944cd285b)
### How to remove NaN values from a dataframe
- I wanted to remove the rows with a precipitation measurement of NaN because there was only a few of them within the dataset and removing them would not alter the information much.
- ![Screenshot 2023-06-11 at 2 24 31 PM](https://github.com/nickpalmer2012/sqalchemy-challenge/assets/128104435/085bf61b-cf3b-4a4c-96d9-4edeeba76d03)

### How do I count values in a session query in sqlalchemy?
- I found this in the SQLAlchemy documentation:
- ![Screenshot 2023-06-11 at 2 44 43 PM](https://github.com/nickpalmer2012/sqalchemy-challenge/assets/128104435/7f96f828-f06e-46e2-903d-ea3a636261b2)

### How do I return a count of each station ID next to the station ID in a session query in sqalchemy?
- For this I was able to, again, borrow code from the "Chinhook_db_analysis" in class challenge to utilize count, group_by, and order_by functions to achieve the desired result described above.
- ![Screenshot 2023-06-11 at 3 09 17 PM](https://github.com/nickpalmer2012/sqalchemy-challenge/assets/128104435/afda6fe4-0eba-4d3f-9858-993711f44e14)


## Designing Your Climate App

### Importing dependencies
- I looked back in the class activity named "Ins_flask_with_ORM" to borrow the code I need to import the necessary dependencies.

### Converting the precipitation scores query for 1 year to a dictionary with the dates as the key and the precipitation as the value:
- For this, I had to consult chat GPT to show me the way. Please see the question and result I received from the great Chat GPT:
- ![Screenshot 2023-06-11 at 6 10 02 PM](https://github.com/nickpalmer2012/sqalchemy-challenge/assets/128104435/8d074b14-35ac-41a2-9a9c-15e1552f1f07)

