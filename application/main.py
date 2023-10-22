"""FastAPI starter sample: Protected endpoint
"""

from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer
import http.client
from .utils import VerifyToken

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()

app = FastAPI()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! "
                "You don't need to be authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result


@app.get("/api/getaccesstoken")
def getaccesstoken():
    """get access token"""

    conn = http.client.HTTPSConnection("dev-iv8rw4nt7rjnc0cg.us.auth0.com")

    payload = "{\"client_id\":\"zHUsmaflyabZMI3Ug63QexxSrvqooXpE\",\"client_secret\":\"IQWQWBYl4l9HPGedb734-w99Mq8-9IqyjxOLdfckG3kIqqcchm1LOXlLIt3mLzZ1\",\"audience\":\"https://test.sam.api.com\",\"grant_type\":\"client_credentials\"}"

    headers = { 'content-type': "application/json" }

    conn.request("POST", "/oauth/token", payload, headers)
 
    res = conn.getresponse()
    data = res.read()

   
    result  = data.decode("utf-8")
    

    return result
