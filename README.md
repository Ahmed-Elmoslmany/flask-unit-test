# This is a demo unit test just for educational porpuse
## How to install
- First of all, make sure these tools are installed: git, pip, flask, flask_sqlalchem.
- Clone this Repo `git clone git@github.com:Ahmed-Elmoslmany/flask-unit-test.git`
- Run this command `cd flask-unit-test`
- open using VS Code `code .` 
- open terminal inside VS code and run `export FLASK_APP=app && flask shell`
- The shell should open now hit this command `from app import db, Book` press enter then run this `db.create_all()`
- Close this terminal and open another one
- Run the server using `flask run` keep this running and open another one
- Run the test using `python3 -m unittest test_app.py`
