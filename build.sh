#!/usr/bin/env bash
echo "setting up the environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Environment setup complete. Run the app with: python app.py"

