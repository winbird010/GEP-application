#!/usr/bin/env bash
set -o errexit

echo ">>> Installing backend deps..."
cd backend
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Running Alembic upgrade..."
alembic upgrade head

echo ">>> Build complete!"