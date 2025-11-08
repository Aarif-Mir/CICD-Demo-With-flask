
#  Flask CI/CD Pipeline with Docker and GitHub Actions

This project demonstrates a simple Flask web application integrated with a complete CI/CD pipeline using GitHub Actions and Docker Hub. Each time code is pushed to the `main` branch, GitHub Actions automatically runs tests, builds a Docker image, and pushes it to Docker Hub.

---

##  Project Structure

The project includes:

* `app.py` – Flask application
* `test_app.py` – Unit tests for validation
* `requirements.txt` – Python dependencies
* `Dockerfile` – Instructions to build the Docker image
* `.github/workflows/ci.yml` – GitHub Actions workflow file

---

##  Flask Application

A simple Flask app provides basic API routes and JSON responses. It’s lightweight and suitable for demonstrating CI/CD automation.

---

##  Testing

Unit tests are written with **pytest** to verify API endpoints and responses.
When the CI workflow runs, tests are executed automatically before any Docker image is built or deployed.

---

##  Docker Setup

The Dockerfile defines how to containerize the Flask app, installs dependencies, and exposes port 5000.
You can build and run it locally with Docker commands. Once running, the app is accessible at `http://localhost:5000`.

---

##  GitHub Actions CI/CD Pipeline

The CI/CD pipeline performs the following steps automatically:

1. **Trigger:** Runs on every push or pull request to the `main` branch.
2. **Build and Test:** Installs dependencies and runs all tests.
3. **Docker Setup:** Configures Docker Buildx for efficient and multi-platform builds.
4. **Authentication:** Logs into Docker Hub using secure access tokens stored in GitHub Secrets.
5. **Build and Push:** Builds the Docker image and pushes it to your Docker Hub repository.

The workflow uses two jobs:

* `build-and-test` – responsible for testing the app
* `docker` – builds and pushes the image (depends on successful tests using `needs:`)

---

##  GitHub Secrets Setup

Before running the workflow, set up the following secrets in your GitHub repository:

* **DOCKERHUB_USERNAME:** your Docker Hub username
* **DOCKERHUB_TOKEN:** an access token generated from Docker Hub (under Account Settings → Security → Access Tokens)

These secrets allow the workflow to log in to Docker Hub securely without exposing credentials.

---

##  Docker Hub Integration

When the workflow completes successfully, a new image is pushed to your Docker Hub repository.
You can pull the image from Docker Hub using your repository name and the `latest` tag.

---


## 🏁 Summary

| Feature           | Description                                            |
| ----------------- | ------------------------------------------------------ |
| Automated Testing | Runs unit tests using pytest                           |
| Containerization  | Flask app built and packaged using Docker              |
| CI/CD             | Automated workflow via GitHub Actions                  |
| Security          | Uses Docker Hub access tokens stored in GitHub Secrets |
| Deployment        | Docker image automatically pushed to Docker Hub        |
