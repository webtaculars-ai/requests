export function cookieHandler(req, res, next) {
  if (!req.session) {
    console.error('Session middleware must be initialized before cookieHandler.');
    return next();
  }

  try {
    // Store the original set-cookie method
    const originalSetCookie = res.setHeader.bind(res);
  
    // Override the set-cookie method to capture and manage cookies for the current request
    res.setHeader = (name, value) => {
      if (name.toLowerCase() === 'set-cookie') {
        if (!Array.isArray(value)) {
          value = [value];
        }
        // Process cookies here (e.g., filtering, modification) before setting them
        // For this scenario, we'll assume a function that filters or modifies cookies as needed
        const processedCookies = processCookiesForRequest(value);
  
        // Call the original set-cookie method with processed cookies
        originalSetCookie('Set-Cookie', processedCookies);
      } else {
        // For all other headers, use the original method
        originalSetCookie(name, value);
      }
    };
  
    console.log('Cookie handler middleware initialized successfully.');
  } catch (error) {
    console.error('Error initializing cookie handler middleware:', error.message, error.stack);
  }

  // Continue to the next middleware or route handler
  next();
}

function processCookiesForRequest(cookies) {
  // Implement any necessary logic to handle cookies for the current request.
  // This could involve filtering out cookies not meant to be persisted, etc.
  // For simplicity, we're returning the cookies unmodified, but this function
  // is where you'd ensure cookies are correctly handled per request.
  try {
    console.log('Processing cookies for the current request.');
    return cookies;
  } catch (error) {
    console.error('Error processing cookies for the current request:', error.message, error.stack);
    return []; // Return an empty cookie array in case of error to prevent potential cookie leakage
  }
}