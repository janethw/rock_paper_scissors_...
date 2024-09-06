# Rock Paper Scissors...And More!

This console app allows the user to create new variants of the traditional Rock Paper Scissors game. It uses the RPS101 
API at: https://rps101.pythonanywhere.com/api

## Getting Started

The import requirements for this console app are set out in the requirements.txt file. The RPS-101 APO is light
on usage limits and licensing requirement. At the time of production, March 2024, there were no usage limits and no
requirement for a key. Developers are warned that this may change soon, but the instructions here were correct at the
time of development.

## Usage

The game works best if you maximise your Python Console on your screen. To run the game, simply run the rps.py file in your preferred IDE. You will be able to create your very own variant of 
Rock Paper Scissors and then play that version against the computer.

## Installations

An installation is required for the requests library:
- Details of the library and install here: https://pypi.org/project/requests/
- `$ python -m pip install requests`

## Additional tech info

The RPS-101 API has three endpoints as follows:

- GET - object array. This endpoint gives a json array of the 101 objects.
- GET - object outcomes. This endpoint gives a json array of the winning outcomes for a given object.
  - URL Parameter (string): object name
- GET - match result. This endpoint gives you the result of a match between two objects.
  - URL Parameters (both strings): object_one, object_two

## Small point

There are a couple of spelling errors in the API objects - while noted, they are not corrected in this code.

## Acknowledgements

Kudos to David C. Lovelace for developing the original RPS-101 concept. This included the 101 hand gestures, the 
artwork for each and the creation of the links between all the different hand gestures. Appreciation to the unnamed 
coder who coded up Lovelace's work and made it available through the RPS-101 API.

## Code Features
- boolean values and if...else statements (eg lines 183-195, 229-238)
- data structure (eg lines 75. 80, 156)
- for and while loops (eg lines 162-165, 169-170, 183-195)
- functions with returns (eg, lines 63-66, 71-87, 91-104, 142-143, 209-221)
- string slicing: start animation at lines 24-37)
- two inbuilt-functions. Examples at:
  - input() at lines 59, 109, 180, 230
  - print() at lines 25, 93-94. 113
  - len() at line 26, 27, 81
- free API: RPS-101 @ https://rps101.pythonanywhere.com/api
- explanation of usage of api in this README.md
- imported modules: requests, random, copy, time, math
- installations required for: requests
- write final results to file: function at line 253-255

## References

RPS-101 API:
- https://rps101.pythonanywhere.com/api

Viewing API endpoints:
- Use of Insomnia: https://insomnia.rest

Python modules:
- Random: https://www.w3schools.com/python/module_random.asp
- Time: https://docs.python.org/3/library/time.html
- Copy: https://docs.python.org/3/library/copy.html

Python string method:
- isalpha(): https://www.w3schools.com/python/ref_string_isalpha.asp

Python list method:
- all(): https://www.freecodecamp.org/news/python-any-and-all-functions-explained-with-examples/

Exception handling for the Requests module adapted from StackOverflow and tutorialspoint.com.
Refs:
- https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
- https://www.tutorialspoint.com/exception-handling-of-python-requests-module#:~:text=Basic%20Exception%20Handling&text=The%20requests.,status%20code%20is%20not%20successful.




