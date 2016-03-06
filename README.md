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





		user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
	worker_connections 768;
	# multi_accept on;
}

#error_log	/var/log/nginx.error_log info;
#root		/home/box/web/

http {
    server {
    	listen 80 default_server;
    	#server_name localhost;
    	#access_log	/var/log/nginx.access_log;
    	location 	^~ /uploads/ {
    		alias	/home/methyst/PycharmProjects/Gihub/web_stepic/uploads/;
		    #alias 	/home/box/web/uploads;
		}
  #   	location 	~* \/[u]\w*\/\w+.\w+$ {
  #   		alias	/home/methyst/PycharmProjects/Gihub/web_stepic/uploads;
		#     #alias 	/home/box/web/uploads;
		# }
		location 	~* \.(jpg|jpeg|gif|png)$ {
			root 	/home/methyst/PycharmProjects/Gihub/web_stepic/public/;
			#root	/home/box/web/public;
		}
		# location	/ {
		# 	return 404;
		# }
    }
}