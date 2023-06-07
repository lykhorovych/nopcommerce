rem python -m venv venv
rem cd venv/Scripts/activate.bat
rem pip install -r requirements.txt
pytest -v -s tests/test_login.py

rem pytest -v -s tests/test_adminpage.py