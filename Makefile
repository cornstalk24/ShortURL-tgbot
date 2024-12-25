# Команды для управления проектом

# Инициализация окружения для разработки
init_dev:
	@python3 -m venv .venv
	@. .venv/bin/activate; pip install --upgrade pip -r requirements.txt

# Запуск контейнера
run:
	@mkdir -p data && chmod 777 data
	@docker compose up -d --build

# Остановка контейнера
stop:
	@docker compose stop

# Удаление контейнера
clean:
	@docker compose down --remove-orphans

# Удаление всех образов и промежуточных данных
prune:
	@docker system prune -a --volumes -f
