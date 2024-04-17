import { cookieHandler } from '../../middlewares/cookieHandler';

export default function handler(req, res) {
  try {
    // Apply the cookie handling middleware
    cookieHandler(req, res, () => {
      // Your API logic here
      console.log('Processing API request in /api/example.');
      res.status(200).json({ message: 'This is an example API route.' });
    });
  } catch (error) {
    console.error('Error handling request in /api/example:', error.message, error.stack);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}