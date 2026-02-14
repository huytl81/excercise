#!/bin/bash

if [[ ! -d certs ]]
then
    mkdir certs
    cd certs/
    if [[ ! -f localhost.pfx ]]
    then
        dotnet dev-certs https -v -ep localhost.pfx -p fe667b70-a174-4cd7-a93d-7d264e0a8da7 -t
    fi
    cd ../
fi

docker-compose up -d
