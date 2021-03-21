## Data2bots Technical Assessment

#### Files
* solution.py : contains my solution in a python file
* solution.ipnb : contains my solution in a python notebook (can be opened using a Jupyter Notebook)
* test_solution.py : contains the testcases for the solution
  
#### Requirements
The only requirements are 
* Pandas
* pytest
* coverage

#### steps to test solution
* Clone this repo `git clone https://github.com/esiebomaj/Data2bots-assessment.git` on your local machine
  <br>
* Optionally you may wish to create a virtual enviroment and then install requirements with `pip install -r requirements.txt` (this step is not nessesary as the requirements are just pandas, pytest, coverage)
  <br>
* To run tests enter `pytest` in colsole
* To check the test coverage enter `coverage run -m --include=./solution.py pytest` in console
*  And then enter `coverage report` in console to view coverage report