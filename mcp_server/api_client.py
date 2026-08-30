import httpx
from mcp_server.settings import settings

# This class is used to make API requests to the FastAPI backend server
class APIClient:

    def __init__(self):
        self.base_url = settings.BACKEND_URL.rstrip("/")
        self.timeout = settings.REQUEST_TIMEOUT

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ):
        try:
            timeout = kwargs.pop("timeout", self.timeout)
            response = httpx.request(
                method=method,
                url=f"{self.base_url}{endpoint}",
                timeout=timeout,
                **kwargs,
            )

            response.raise_for_status()

            return response.json()

        except httpx.ConnectError:

            raise Exception(
                "FastAPI Backend is not running."
            )

        except httpx.HTTPStatusError as e:

            try:
                detail = e.response.json()
            except Exception:
                detail = e.response.text

            raise Exception(
                f"Backend Error ({e.response.status_code}): {detail}"
            )

        except Exception as e:

            raise Exception(str(e))

    # -------------------------
    # HTTP Methods
    # -------------------------

    def get(
        self,
        endpoint: str,
        params: dict | None = None,
    ):
        return self._request(
            "GET",
            endpoint,
            params=params,
        )

    def post(
        self,
        endpoint: str,
        json: dict | None = None,
    ):
        return self._request(
            "POST",
            endpoint,
            json=json,
        )

    def put(
        self,
        endpoint: str,
        json: dict | None = None,
    ):
        return self._request(
            "PUT",
            endpoint,
            json=json,
        )

    def delete(
        self,
        endpoint: str,
    ):
        return self._request(
            "DELETE",
            endpoint,
        )


api_client = APIClient()