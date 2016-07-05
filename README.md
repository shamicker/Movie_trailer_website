# Create a Movie Website 
### Stage 3 project for Udacity's 'Intro to Programming Nanodegree'

Aim of the project:
- Write code to store a list of your favorite movies, including box art imagery and a movie trailer URL. 
- Use your code to generate a static web page allowing visitors to browse their movies and watch the trailer.

How will I complete this project?
- If you haven't already, install Python
- Create a data structure (i.e. a Python Class) to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
- Create multiple instances of that Python Class to represent your favorite movies; group all the instances together in a list.
- To help you generate a website that displays these movies, we have provided a Python module called [fresh_tomatoes.py](https://github.com/adarsh0806/ud036_StarterCode)
  - this module has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.
- Ensure your website renders correctly when you attempt to load it in a browser.

Your submission will be evaluated according to the following rubric.

## PROJECT SPECIFICATION
### Functionality

**Content**
- Page presents all required content (movie title, poster art, and trailer link)

**Python Data Structure**
- Page is dynamically generated from a Python data structure

**Errors**
- Page is free of errors, glitches, and bugs

### Code Review

**Use of Variables**
- Code uses variables to avoid magic numbers
- Each variable name reflects the purpose of the value stored in it
- Once initiated, the purpose of each variable is maintained throughout the program
- No variables override Python built-in values (for example, def)

**Use of Functions**
- Functions are used as tools to automate tasks which are likely to be repeated
- Functions produce the appropriate output (typically with a return statement) from the appropriate input (function parameters)
- No functions are longer than 18 lines of code (does not include blank lines, comments, or function and variable definitions)

**Appropriate Use of Data**
- The appropriate data types are used consistently (strings for text, lists for ordered data, nested lists as appropriate)

**Appropriate Use of Coding Techniques**
- Student demonstrates coding techniques like branching and loops appropriately (i.e. to loop through a list, for element in list:; or to test whether something is in a list, if name in list_names:)

**Appropriate Use of Classes**
- Code defines classes properly and uses instances of those classes in the code

**Comments / Documentation**
- Each function includes a comment which explains the intended behavior, inputs, and outputs (if applicable)

### Suggestions to Make Your Project Stand Out!
Add additional information about your favorite movies (screenwriters, release date, etc.) and modify fresh_tomatoes.py to display it on your web page

