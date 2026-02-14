docker network create abpsolution2 --label=abpsolution2
docker-compose -f containers/redis.yml up -d
exit $LASTEXITCODE