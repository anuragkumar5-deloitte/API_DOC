import responses
import requests
from Utils import EndPoints

@responses.activate
def test_trigger_pulse_time():
    resp = responses.Response(
        method="POST",
        url=EndPoints.BaseUrl + EndPoints.post_trigger_pulse_time,
        status=200,
        json={
            "sec": 1234,
            "nsec": 1234
        }
    )

    responses.add(resp)

    req = requests.post(EndPoints.BaseUrl + EndPoints.post_trigger_pulse_time)
    print(req.text)