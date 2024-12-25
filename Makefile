# Default target
all: run

# Initialize the development environment
init_dev:
	python3 -m venv .venv
	. .venv/bin/activate; pip install --upgrade pip -r requirements.txt

# Run the application using Docker Compose
run:
	@mkdir -p data && chmod 777 data
	docker compose up -d --build

# Stop the application
stop:
	docker compose down

# Clean up Docker containers and volumes
clean:
	docker compose down --volumes --remove-orphans

# View logs
logs:
	docker compose logs -f
