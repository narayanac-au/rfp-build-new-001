db_engine=$1
db_username=$2
db_pw=$3
db_host=$4
db_name=$5
db_port=$6

# declare prod.env file path
env_file=".env/prod.env"

# append key and secrets in prod.env
echo SQL_ENGINE=$db_engine >> $env_file
echo SQL_DATABASE=$db_name >> $env_file
echo SQL_USER=$db_username >> $env_file
echo SQL_PASSWORD=$db_pw >> $env_file
echo SQL_HOST=$db_host >> $env_file
echo SQL_PORT=$db_port >> $env_file