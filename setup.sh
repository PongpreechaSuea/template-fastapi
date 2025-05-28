#!/bin/bash
ENV_NAME="tfapi"
PYTHON_VERSION="3.9.16"

if ! command -v conda &> /dev/null
then
    echo "Conda not found. Please install Conda first."
    exit 1
fi

echo "Creating Conda environment: $ENV_NAME with Python $PYTHON_VERSION"
conda create --name $ENV_NAME python=$PYTHON_VERSION -y

echo "Activating environment: $ENV_NAME"
conda activate $ENV_NAME

if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt"
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

echo "Setup completed. Conda environment $ENV_NAME is ready to use."
