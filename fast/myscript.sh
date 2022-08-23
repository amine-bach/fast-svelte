#!/bin/bash

uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"

cd front
npm install
npm run build

<<<<<<< HEAD

#end
=======
##
>>>>>>> 36e0aff2a1833dd68b7935b7a8ca6eb90a7ab72b
