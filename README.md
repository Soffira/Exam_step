# Run it

Необходимо запустить следующую команду для запуска:

$ docker run --name cherrypy -d -p 8080:8080 lawouach/cherrypy-hello-world

Вы можете перейти по ссылке в браузере http://127.0.0.1:8080/api/users

Для просмотра логов используется команда:

$ docker logs cherrypy

Для остановки сервера можно использовать следующую команду:

$ docker stop cherrypy

# Build it

Для того, чтобы создать образ:

$ docker build -t MYREPO/IMAGE_NAME .
