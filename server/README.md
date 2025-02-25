# Weather Forecast Server

This is the backend server for the Weather Forecast application. It's built with Python and provides weather forecast data through a REST API.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Create and activate a virtual environment (recommended):

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

1. Make sure your virtual environment is activated (if you're using one)

2. Start the server:

```bash
python server.py
```

The server will start running on `http://localhost:3000` by default.

## Available Endpoints

- `GET /forecast` - Returns weather forecast data

## Troubleshooting

If you encounter any issues:

1. Make sure you're using Python 3.x
2. Verify that your virtual environment is activated
3. Ensure all dependencies are installed correctly
4. Check that port 5000 is not being used by another application 
