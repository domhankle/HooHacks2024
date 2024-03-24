#!/bin/bash
echo "Removing db..."

rm ../backend/healthapp/db.sqlite3

auto_migrate.sh