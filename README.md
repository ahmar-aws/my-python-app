# Python Application

A simple Python REST API application using Flask.

## Features

- REST API with multiple endpoints
- Health check endpoint
- Request/response handling
- Error handling
- Unit tests with pytest
- GitHub Actions CI/CD pipeline

## Installation
```bash
pip install -r requirements.txt
```

## Running Application
```bash
python app.py
```

Application runs on `http://localhost:5000`

## API Endpoints

- `GET /` - Home endpoint
- `GET /health` - Health check
- `POST /api/greet` - Greeting (requires name in JSON)
- `GET /api/info` - Application info

## Testing
```bash
pytest test_app.py -v
```

## Environment Variables

- `DEBUG` - Enable debug mode (default: False)
- `PORT` - Server port (default: 5000)
- `ENVIRONMENT` - Environment name (default: development)

## CI/CD

This project uses GitHub Actions for:
- Automated testing
- Code quality checks
- Deployment on push to main

See `.github/workflows/ci.yml` for configuration.
