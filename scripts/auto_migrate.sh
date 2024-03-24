#!/bin/bash
echo "Migrating..."

python3 ../backend/healthapp/manage.py makemigrations

python3 ../backend/healthapp/manage.py migrate