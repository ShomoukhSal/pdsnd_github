>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
14-DEC-2022

### Project Title
Data Exploration on U.S. Bikeshare Database 

### Project Overview
I used this project as an opportunity to practice Python by exploring U.S. bikeshare system database for 3 U.S. cities: New York city, Chicago, and Washington.
So, to effectively analyze the descriptive statistics, IÕve built code to import the data and answer key questions about the use of this system. 
Additionally, I've created a script that accepts raw input to create an interactive user experience to provide this information in the terminal. 

### Softwares used for this project: 
- Anaconda, then I installed Python 3, NumPy, and pandas. 
- Atom: a text editor 
- A terminal application (Terminal on Mac) 

### Files used
- chicago.csv
- new_york_city.csv
- washington.csv

### Program Details 
The program asks the user to enter the city they want to view the data from (e.g., Chicago, New York, or Washington), enter the month they want to view the data from (options: from January to June), and enter the day they want to view the data from (e.g., Sunday), also, there is an option to enter ÒAllÓ if they want to view all the days and the months available.
After the user input, the following details are printed:
1- The most frequent times of travel:
- Most popular month
- Most popular day of week
- Most popular hour of day
2- Popular stations and trip:
- Most popular start station.
- Most popular end station.
- Most common combination of Start Station and End Station trip
3- Trip duration:
- Total travel time
- Average travel time
4- User information:
- Counts of user types
- Counts of gender. 
- Earliest birth year.
- Most recent birth year.
- Most common birth year.
NOTE: Gender & Birth Year Columns only available in new_york_city.csv and chicago.csv. Thus, if the user entered ÒWashingtonÓ it will print (This file does not contain a 'Birth Year' column.) & (This file does not contain a 'Gender' column.)

After that, the user is asked if they want to view the raw data (the first 5 rows of data) or not. 
Finally, the user is given the option to restart the program or not.

### Credits
- https://numpy.org/devdocs/user/absolute_beginners.html#how-to-create-a-basic-array
- https://pymotw.com/3/ 
- Udacity: The instructors in Udacity & Data Analyst Nanodegree program. 

