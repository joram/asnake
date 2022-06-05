build:
	docker build . -t joram87/asnake

push:
	docker push joram87/asnake

pull_on_server:
	ssh 192.168.1.222 "cd projects/nas; docker-compose pull asnake"

update_on_server:
	ssh 192.168.1.222 "cd projects/nas; docker-compose up -d asnake"

tail_logs_on_server:
	ssh 192.168.1.222 "cd projects/nas; docker-compose logs -f asnake"

deploy: build push pull_on_server update_on_server tail_logs_on_server