export_token:
	GITHUB_TOKEN=$(cat github_token) && export GITHUB_TOKEN

checkout_client:
	cd client && sh checkout.sh

dev:
	make export_token && make checkout_client && docker compose up --build