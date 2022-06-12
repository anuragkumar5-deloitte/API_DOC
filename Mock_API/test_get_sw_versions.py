import responses
import requests
from responses.registries import OrderedRegistry
from Utils import EndPoints

@responses.activate(registry=OrderedRegistry)
def test_sw_versions():
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_sw_versions,
                json={"msg": "Success"}, status=200,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_sw_versions,
                json={"msg": "Internal Server Error"},status=500,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_sw_versions,
                json={"msg": "Unauthorized"},status=401,
            )
            responses.add(
                responses.GET,
                EndPoints.BaseUrl+EndPoints.get_sw_versions,
                json={"msg": "Bad request"},status=400,
            )

            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_sw_versions)
            print(resp.json())
            assert resp.status_code == 200
            assert resp.json() =={"msg": "Success"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_sw_versions)
            assert resp.status_code == 500
            assert resp.json() =={"msg": "Internal Server Error"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_sw_versions)
            assert resp.status_code == 401
            assert resp.json() =={"msg": "Unauthorized"}
            resp = requests.get(EndPoints.BaseUrl+EndPoints.get_sw_versions)
            assert resp.status_code == 400
            assert resp.json() =={"msg": "Bad request"}

