#!/bin/bash
uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"

cd front
npm install
npm run build
