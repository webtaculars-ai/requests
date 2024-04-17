import pytest
from requests.sessions import Session
from pytest_requests_mock import Mocker

def test_request_cookies_not_persisted_to_session(requests_mock: Mocker):
    # Mock the URL for testing
    test_url = "https://mockserver.local"
    requests_mock.get(test_url, text="response")

    # Create a session object
    session = Session()

    # Make the first request with specific cookies
    session.get(test_url, cookies={"session_id": "123456"})

    # Make another request to the same URL without specifying cookies
    response = session.get(test_url)

    # Assert that the cookies from the first request are not present in the second request
    assert "session_id" not in session.cookies, "Session incorrectly persists request-specific cookies across requests."

    # Optionally, check the response cookies to ensure they do not include the cookies from the first request
    assert "session_id" not in response.cookies, "Response incorrectly includes request-specific cookies."