@echo off
cd /d %~dp0
start cmd /k "python manage.py runserver"
timeout /t 5 /nobreak > NUL
start "" "http://127.0.0.1:8000"
