# Weather Forecast Client

This is the frontend client for the Weather Forecast application. It's built with React and Vite, providing a modern web interface for viewing weather forecast data.

## Prerequisites

- Node.js (version specified in `.node-version`)
- npm (comes with Node.js)

## Setup

1. Install dependencies:

```bash
npm install
```

## Development

To run the development server:

```bash
npm run dev
```

This will start the development server on `http://localhost:5173` by default. The page will automatically reload if you make changes to the code.

## API Integration

The client connects to the backend server running on `http://localhost:3000` by default. Make sure the backend server is running before starting the client.

The backend server is located at `server/`

## Troubleshooting

If you encounter any issues:

1. Make sure you're using the correct Node.js version (check `.node-version`)
2. Verify all dependencies are installed (`npm install`)
3. Check that the development server port (5173) is not in use
4. Ensure the backend server is running and accessible 
