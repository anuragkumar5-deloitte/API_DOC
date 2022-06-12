import responses
import requests
from Utils import EndPoints

@responses.activate
def test_post_imx_register():
    resp = responses.Response(
        method="POST",
        url=EndPoints.BaseUrl+EndPoints.post_imx_register,
        status=200,
        json={"register": "0x01", "register_value": "100"},
    )

    responses.add(resp)

    req = requests.post(EndPoints.BaseUrl+EndPoints.post_imx_register)
    print(req.text)

