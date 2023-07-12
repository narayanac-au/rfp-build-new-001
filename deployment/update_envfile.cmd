setlocal

@echo on

@REM  config files
set env_file=".env/prod.env"

@REM  command line arguments
set db_engine=$1
set db_username=$2
set db_pw=$3
set db_host=$4
set db_name=$5
set db_port=$6


@REM append key and secrets in prod.env
echo SQL_ENGINE=%db_engine% >> %env_file%
echo SQL_DATABASE=%db_name% >> %env_file%
echo SQL_USER=%db_username% >> %env_file%
echo SQL_PASSWORD=%db_pw% >> %env_file%
echo SQL_HOST=%db_host% >> %env_file%
echo SQL_PORT=%db_port% >> %env_file%