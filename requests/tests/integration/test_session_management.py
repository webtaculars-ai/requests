import logging
from http_library import Session

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_cookie_persistence():
    session = Session()
    
    try:
        # First request with specific cookies
        response1 = session.get('https://example.com/set-cookie', cookies={'test': 'cookie'})
        logging.info('First request sent to set cookie.')
        
        # Second request to check if the cookie persists
        response2 = session.get('https://example.com/check-cookie')
        logging.info('Second request sent to check cookie persistence.')

        # Assert that the 'test' cookie does not persist beyond the first request
        assert 'test=cookie' not in response2.request.headers.get('Cookie', ''), "Cookie 'test' persisted beyond the first request, which is not expected."

        logging.info('Cookie persistence test passed: Test cookie does not persist beyond the first request.')
    except AssertionError as e:
        logging.error(f'Assertion Error: {e}')
        raise
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise