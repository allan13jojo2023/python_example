# upgrade all python packages
pip freeze > requirements.txt
pip install -r requirements.txt --upgrade


# add environment variables
touch ~/.bash_profile; open ~/.bash_profile
source ~/.bash_profile


prefect orion database reset -y
prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="sqlite+aiosqlite:////full/path/to/a/location/orion.db"
prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:yourTopSecretPassword@localhost:5432/orion"
docker:
docker run -d --name orion_postgres -v oriondb:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=orion postgres:latest

# change prefect database config
prefect orion database reset -y
prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:test2017@localhost:5433/postgres"

prefect config view --show-sources
prefect orion start


create EXTENSION pgcrypto;

