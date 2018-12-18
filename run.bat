@echo off

set env_folder=env
echo -------------------------------------------------------------------------------
echo Default Python Virtual Environment is ^/%env_folder%


:ask
echo -------------------------------------------------------------------------------
echo Press [1] for Skipping project environment Setup
echo Press [2] for Preparing project environment Setup

set choice1Timeout=10
set defaultChoice1=1
choice /t %choice1Timeout% /c 12 /N /d %defaultChoice1% /m "(Decision will be %defaultChoice1% after %choice1Timeout% seconds) Your Choice ?"
rem The construct if errorlevel n checks if the errorlevel is at least n, therefor the way to do the test is go from higher errorlevel to lower errorlevel
if errorlevel 2 goto setupEnv
if errorlevel 1 goto skipSetupEnv


:setupEnv

if exist "%env_folder%\" (
    echo.
    echo -------------------------------------------------------------------------------
	echo ^ ^ ^> skipping creating python virtual environment
	echo -------------------------------------------------------------------------------
	echo [%env_folder%] Exists !
) else (

	rd /s /q "%env_folder%"
	echo.
	echo -------------------------------------------------------------------------------
	echo ^ ^ ^> creating python virtual environment [%env_folder%]
	echo -------------------------------------------------------------------------------
	python -m venv %env_folder%
)

echo.
echo -------------------------------------------------------------------------------
echo ^ ^ ^> activating python virtual environment ...
echo -------------------------------------------------------------------------------
call %env_folder%\Scripts\activate
echo virtual environment [%env_folder%] was activated

echo.
echo -------------------------------------------------------------------------------
echo ^ ^ ^> collecting python packages ...
echo -------------------------------------------------------------------------------
call pip install -r requirements.txt --upgrade

:skipSetupEnv

echo.
echo -------------------------------------------------------------------------------
echo ^ ^ ^> activating python virtual environment ...
echo -------------------------------------------------------------------------------
call %env_folder%\Scripts\activate
echo virtual environment [%env_folder%] was activated
