# RMSystemConsumer
MicroServicio encargado de escuchar los eventos reportados por el simulador (RMSystem) y de realizar el llamado al microservicio MeasurementSystemAPI para almacenar las métricas. 


Para ejecutar el microservicio localmente.
1. Garantizar que se tiene una instancia de redis corriendo. 
1. Instalar los requerimientos `pip install -r requirements.txt` en un ambiente virtual
2. Ejectar `python exec.py` desde la carpeta `app`


Para ejecutar el microservicio desde docker:
1. levantar el contenedor con el servicio de redis: [RedisService](https://github.com/OviLuis/RedisService)
1. construir la imagen `consumer_1`. ejecutar `docker build -t consumer_1 .` desde la raiz del proyecto donde esta ubicado el archivo `Dockerfile`
2. ejecutar `docker-compose up -d` desde la raiz del proyecto o donde este ubicado el archivo `docker-compose.yml`
