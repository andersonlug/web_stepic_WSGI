# web_stepic

homework. WEB technology on stepic.org

	git clone https://github.com/your_account/stepic_web_project.git /home/box/web
	bash /home/box/web/init.sh


# NGINX
- читать:
	* http://nginx.org/ru/linux_packages.html
	* http://eax.me/nginx/
	* http://devacademy.ru/posts/razbiraemsya-v-http-proksi-nginx-balansirovke-nagruzki-buferizatsii-i-keshirovanii/

- установка

	apt-get update
	apt-get install nginx

- Конфиг находится:

	/etc/nginx/nginx.conf
	/var/log/nginx/error.log

- Команда на запуск

	sudo /etc/init.d/nginx start
	sudo nginx -s reload # reload config

- проверка ответа
	* curl -I http://localhost:80/uploads/kitten.png
	* wget localhost:80 -O -

- Когда nginx запущен:
	- nginx -s "сигнал":
		top — быстрое завершение
		quit — плавное завершение
		reload — перезагрузка конфигурационного файла
		reopen — переоткрытие лог-файлов

# WSGI

# Gunicorn

- читать
	* http://docs.gunicorn.org/en/stable/deploy.html
	* https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx

- установка
	sudo apt-get install gunicorn

- config
	* http://docs.gunicorn.org/en/latest/configure.html

- запуск (terminal or with setting file)
	* gunicorn hello:app --bind 0.0.0.0:8080   -->  $(MODULE_NAME):$(VARIABLE_NAME)
	* gunicorn -c gunicorn_cfg.py web_application:application
	* sudo /etc/init.d/gunicorn restart
