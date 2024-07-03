# Setting Up CI/CD Pipeline with GitHub Actions

## Introduction

In this tutorial, we will set up a Continuous Integration/Continuous Deployment (CI/CD) pipeline for our Python project using GitHub Actions. This pipeline will automatically run tests whenever we push code to the repository or create a pull request and deploy the application to Google Cloud.

## Step-by-Step Guide

### Step 1: Create the Workflow File

First, create a directory named `.github/workflows` in the root of your project. Inside this directory, create a file named `ci.yml`. This file will define our CI/CD workflow.

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Run tests
      run: |
        source venv/bin/activate
        pytest

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Google Cloud SDK
      uses: google-github-actions/setup-gcloud@master
      with:
        project_id: ${{ secrets.GCP_PROJECT_ID }}
        service_account_key: ${{ secrets.GCP_SA_KEY }}

    - name: Deploy to Google App Engine
      run: gcloud app deploy --quiet
```
## Step 2: Create the Test Cases
Create a file named `test_app.py` in your project directory and add the following content:

```python
import unittest
from OnlineShopping import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```

## Step 3: Ensure Dependencies are Listed
Make sure you have a `requirements.txt` file in your project directory listing all dependencies, including `pytest`.

```plaintext
Flask
pytest
gunicorn
```
## Step 5: Commit and Push Changes
Commit the new workflow file, test cases, and `requirements.txt` to your repository and push the changes.

```bash
git add .github/workflows/ci.yml test_app.py requirements.txt CI_CD_Pipeline.md app.yaml
git commit -m "Add CI/CD pipeline with GitHub Actions and test cases"
git push origin main
```

## Step 6: Verify the Workflow
After pushing the changes, go to your GitHub repository and navigate to the "Actions" tab. You should see the workflow running. If everything is set up correctly, the workflow will run and show the status of your tests, and then deploy the application to Google Cloud.

## Conclusion
By setting up this CI/CD pipeline and adding test cases, we ensure that our code is automatically tested on every push and pull request and deployed to Google Cloud. This helps us catch issues early and maintain a high-quality codebase.


# Without GCP integration at Github Worklow

## Step: Create the Test Cases
Create a file named `test_app.py` in your project directory and add the following content:

```python
import unittest
from OnlineShopping import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```
### Step: Create the Workflow File without GCP

First, create a directory named `.github/workflows` in the root of your project. Inside this directory, create a file named `ci.yml`. This file will define our CI/CD workflow.

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m unittest discover
```
## Step: Commit and Push Changes
```bash
git add .github/workflows/ci.yml test_app.py requirements.txt CI_CD_Pipeline.md
git commit -m "Add CI/CD pipeline with GitHub Actions and test cases"
git push origin main
```

## Verify the Workflow:

After pushing the changes, go to your GitHub repository and navigate to the "Actions" tab. You should see the workflow running. If everything is set up correctly, the workflow will run and show the status of your tests

![CI/CD Pipeline](/CI-CD.JPG)
