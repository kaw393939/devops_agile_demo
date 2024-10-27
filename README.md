# Hello World Demo

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI Status](https://github.com/yourusername/hello-world-demo/workflows/CI/badge.svg)](https://github.com/yourusername/hello-world-demo/actions)

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [Setup and Installation](#setup-and-installation)
* [Running the Application](#running-the-application)
* [Running Tests](#running-tests)
* [Continuous Integration](#continuous-integration)
* [Project Structure](#project-structure)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

## Project Overview

**Hello World Demo** is a simple web application built with Flask that displays a "Hello World" message and includes a basic calculator. The calculator supports addition, subtraction, multiplication, and division operations. This project demonstrates best practices in web development, automated testing, and Continuous Integration (CI) using GitHub Actions.

## Features

* **Flask Web Application**
  * Serves a static HTML page
  * Displays "Hello World" message
  * Includes functional calculator

* **Calculator Functionality**
  * Addition
  * Subtraction
  * Multiplication
  * Division

* **Automated Testing**
  * Unit Tests: Verify individual calculator functions
  * Integration Tests: Test Flask routes and calculator integration
  * End-to-End Tests: Simulate user interactions using Playwright

* **Continuous Integration**
  * GitHub Actions pipeline
  * Automated testing on every commit
  * Quality checks before merging

## Technology Stack

* **Backend**
  * Python
  * Flask

* **Frontend**
  * HTML
  * CSS
  * JavaScript

* **Testing**
  * Pytest
  * Playwright

* **CI/CD**
  * GitHub Actions
  * Git

## Setup and Installation

### Prerequisites

* Python 3.7 or higher ([Download](https://www.python.org/downloads/))
* Git ([Download](https://git-scm.com/downloads))

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hello-world-demo.git
   cd hello-world-demo
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   * macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   * Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running the Application

1. Ensure your virtual environment is active:
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

3. Open [http://localhost:5000](http://localhost:5000) in your browser

## Running Tests

Ensure your virtual environment is active before running tests.

### Unit Tests

```bash
pytest tests/unit/
```

### Integration Tests

```bash
pytest tests/integration/
```

### End-to-End Tests

```bash
pytest tests/e2e/
```

> **Note:** The `flask_server` fixture automatically manages the Flask server during E2E tests.

## Continuous Integration

GitHub Actions automates our testing pipeline. The workflow:

1. Triggers on:
   * Push to main branch
   * Pull request to main branch

2. Executes:
   * Code checkout
   * Python setup
   * Dependencies installation
   * Unit tests
   * Integration tests
   * E2E tests

View CI status in the [Actions tab](https://github.com/yourusername/hello-world-demo/actions)

## Project Structure

```
hello-world-demo/
├── .github/
│   └── workflows/
│       └── test.yml
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── e2e/
│   ├── integration/
│   └── unit/
├── app.py
├── calculator.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Key Files

* `app.py`: Main Flask application
* `calculator.py`: Calculator functionality
* `pytest.ini`: Pytest configuration
* `requirements.txt`: Project dependencies
* `.github/workflows/test.yml`: CI workflow definition

## Troubleshooting

### Unknown Pytest Marker

**Problem:** `PytestUnknownMarkWarning: Unknown pytest.mark.e2e`

**Solution:** Create/update `pytest.ini`:
```ini
[pytest]
markers =
    e2e: mark test as end-to-end test
```

### Port Conflicts

**Problem:** Port 5000 is in use

**Solution:**
1. Kill existing process:
   ```bash
   pkill -f "python app.py"
   ```

2. Or change port in `app.py`:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, port=5001)
   ```

### Virtual Environment Issues

**Solution:**
```bash
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

## Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> **Note:** Replace `yourusername` with your actual GitHub username in all URLs.
