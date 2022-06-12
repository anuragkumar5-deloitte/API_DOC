import responses
import requests
from Utils import EndPoints

@responses.activate
def test_post_enable_trigger_value_pulse():
    resp = responses.Response(
        method="POST",
        url=EndPoints.BaseUrl+EndPoints.post_enable_trigger_value_pulse,
        status=200,
        json={
            "enable":1
        },
    )

    responses.add(resp)

    req = requests.post(EndPoints.BaseUrl+EndPoints.post_enable_trigger_value_pulse)
    print(req.text)
    assert req.status_code == 200