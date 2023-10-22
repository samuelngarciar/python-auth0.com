# Protecting your FastAPI API with Auth0

## Running the example

In order to run the example you need to have `python3` (any version higher than `3.6`) and `pip3` installed.

### Configuration
First
For development purpose must be create a free account in auth0.com and after create a Applications API like this:
![image](https://github.com/samuelngarciar/python-auth0.com/assets/84947793/026f4b7b-d83c-42a6-8211-8ece4363af1d)


The configuration you'll need is mostly information from Auth0, you'll need both the tentant domain and the API information.

This app reads its configuration information from a `.config` file by default.

To create a `.config` file you can copy the `.example.config` file and fill the values accordingly:

```console
cp .example.config .config
# update the config file for the correct values
export ENV='.config'
```

You can change this behavior by setting the following environment variables (remember to update the values accordingly):
Note. The advantage here is the this is generic, in others word that values can be uptated with the data of any auth02 provider
```console
export ENV='variables'
export DOMAIN='your.domain.auth0.com'
export API_AUDIENCE='your.api.audience'
export ISSUER='https://your.domain.auth0.com'
export ALGORITHMS='RS256'
```

### Spin up the server

Once you've set your environment information below you'll find the commands you'll need.

1. Create and activate a python environment:

```console
python3 -m venv .env
source .env/bin/bash
```

2. Install the needed dependencies with:

```console
pip install -r requirements.txt
```
3. Start the server with the following:

```console
uvicorn application.main:app
```

4. Try calling [http://localhost:8000/api/public](http://localhost:8000/api/public)

```
curl -X 'GET' \
  'http://localhost:8000/api/public' \
  -H 'accept: application/json'
```

## API documentation

Access [http://localhost:8000/docs](http://localhost:8000/docs). From there you'll see all endpoints and can test your API

## Examples in this repo

| Branch name | Example |
| ----------- | ------- |
| `main` | The starter sample only has two endpoints and one of them needs protection |
| `private` | The result of protecting the first endpoint with Auth0 |
| `private-scoped` | Implemented a protected endpoint with checks for scopes |

Finally you can to get a new access token using the follow method
![image](https://github.com/samuelngarciar/python-auth0.com/assets/84947793/c3fee256-887f-4294-87c8-449fa7a71633)

And using the access token responsed, for invoke the private method follow:
Copy and access token and paste here
![image](https://github.com/samuelngarciar/python-auth0.com/assets/84947793/fd9ea84a-36bb-4bfb-ae70-93edcb3dae54)

Now, you can test the private method such as
![image](https://github.com/samuelngarciar/python-auth0.com/assets/84947793/5a730f43-6436-4442-ac3f-6cbe8b1ef7d9)


