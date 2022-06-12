import responses
import requests
from responses.registries import OrderedRegistry
from Utils import EndPoints

@responses.activate(registry=OrderedRegistry)
def test_rht():
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_rht,
                json={"msg": "Success"}, status=200,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_rht,
                json={"msg": "Internal Server Error"},status=500,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_rht,
                json={"msg": "Unauthorized"},status=401,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_rht,
                json={"msg": "Bad request"},status=400,
            )

            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_rht)
            assert resp.status_code == 200
            # print(resp.json())
            assert resp.json() =={"msg": "Success"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_rht)
            assert resp.status_code == 500
            assert resp.json() =={"msg": "Internal Server Error"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_rht)
            assert resp.status_code == 401
            assert resp.json() =={"msg": "Unauthorized"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_rht)
            assert resp.status_code == 400
            assert resp.json() =={"msg": "Bad request"}