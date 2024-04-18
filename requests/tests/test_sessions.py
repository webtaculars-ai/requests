import pytest
from requests import Session
import requests_mock

@pytest.fixture
def mock_request():
    with requests_mock.Mocker() as m:
        yield m

def test_request_cookie_not_persisted_across_sessions(mock_request):
    """
    Test to ensure that cookies set in individual requests are not
    persisted across sessions unless explicitly intended.
    """
    test_url = "https://example.com/set_cookie"
    mock_request.get(test_url, cookies={'test_cookie': 'test_value'})

    session = Session()

    # Send a request with a specific cookie
    response = session.get(test_url, cookies={'test_cookie': 'test_value'})

    # Ensure the cookie is set for this request
    assert response.cookies.get('test_cookie') == 'test_value'

    # Send another request without setting the cookie explicitly
    response2 = session.get("https://example.com")

    # Verify that the cookie from the first request is not persisted
    assert not response2.cookies.get('test_cookie'), "Cookie was unexpectedly persisted across sessions."

def test_cookie_persistence_intended_behavior(mock_request):
    """
    Test to ensure that when cookies are explicitly added to the session,
    they are persisted across requests as intended.
    """
    test_url = "https://mockserver.local"
    mock_request.get(test_url, text="response")

    session = Session()
    session.cookies.set('persistent_cookie', 'persistent_value')

    # Make a request to the URL
    session.get(test_url)

    # Assert that the persistent cookie is preserved across requests within the session
    assert session.cookies.get('persistent_cookie') == 'persistent_value', "Cookie was not persisted as expected."