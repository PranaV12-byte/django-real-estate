# Real Estate Platform

A robust, full-stack real estate web application designed to streamline property listings, property management, and user interactions. 

## 🚀 Overview
This platform provides a complete solution for real estate operations. Users can browse and filter properties, view detailed listings, submit enquiries directly to agents, and leave ratings. It features a secure authentication system, an intuitive React-based frontend, and an asynchronous task queue for background operations like email dispatch. The entire application is containerised for a seamless, reproducible development and deployment experience.

## 💻 Tech Stack
- **Frontend:** React 17, Redux Toolkit, React-Bootstrap
- **Backend:** Django 3.2, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Caching & Async Queue:** Redis, Celery, Celery Flower
- **Authentication:** Djoser (JWT)
- **Infrastructure:** Docker, Docker Compose, Nginx
- **Code Quality & Testing:** Pytest, Flake8, Black, isort

## 🛠️ Key Features
- **Property Management:** Browse, filter, and search through property listings with pagination and detailed views.
- **Secure Authentication:** JWT-based user registration, login, and email account activation.
- **Asynchronous Tasks:** Celery integration for non-blocking email delivery and background processes.
- **Profiles & Enquiries:** User profile management, property rating system, and direct contact tools for interacting with agents.
- **Fully Dockerised:** A single `make build` command spins up the backend, frontend, database, cache, workers, and reverse proxy perfectly configured together.

## ⚙️ Local Development Quick Start

**Prerequisites:** Docker and Docker Compose must be installed.

1. **Set up environment variables:**
   Copy the example environment file and fill in your secrets.
   ```bash
   cp .env.example .env
   ```
2. **Build and start the containers:**
   Use the provided makefile shortcut to build images and spin up the environment.
   ```bash
   make build
   ```
3. **Run database migrations:**
   ```bash
   make migrate
   ```
4. **Access the application:**
   - App (via Nginx proxy): `http://localhost:8080`
   - Celery Flower Dashboard: `http://localhost:5557`

## 🧹 Useful Make Commands

- `make up` - Start containers without rebuilding
- `make down` - Stop all active containers
- `make createsuperuser` - Create a new admin user
- `make test` - Run the test suite with coverage
