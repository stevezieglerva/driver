cls

call ..\Scripts\activate
call python -m unittest unit_tests.py
set test_error=%ERRORLEVEL%

call deactivate
exit /b %test_error%
