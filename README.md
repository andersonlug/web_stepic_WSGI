# web_stepic
homework. WEB technology on stepic.org

	git clone https://github.com/your_account/stepic_web_project.git /home/box/web
	bash /home/box/web/init.sh


# NGINX
читать:
http://nginx.org/ru/linux_packages.html
http://eax.me/nginx/

установка
apt-get update
apt-get install nginx

Конфиг находится:
/etc/nginx/nginx.conf

Команда на запуск
sudo /etc/init.d/nginx start
проверка ответа
curl -I http://localhost:80/uploads/kitten.png

Когда nginx запущен:
	nginx -s "сигнал":
		top — быстрое завершение
		quit — плавное завершение
		reload — перезагрузка конфигурационного файла
		reopen — переоткрытие лог-файлов
