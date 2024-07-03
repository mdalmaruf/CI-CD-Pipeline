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
