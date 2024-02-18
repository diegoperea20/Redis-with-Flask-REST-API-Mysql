# Redis with Flask REST API Mysql 
<p align="justify">
Redis with Flask REST API Mysql ,where you create title and description.
</p>

[ REST API WITHOUT REDIS](https://github.com/diegoperea20/Flask-REST-API-Organized)


```python
python main.py
```
<p align="center">
  <img src="README-images\example-REST.png" alt="StepLast">
</p>



## WITHOUT REDIS 
<p align="center">
  <img src="README-images\without-redis-only-mysql.PNG" alt="StepLast">
</p>



## WITH REDIS 
<p align="center">
  <img src="README-images\with-redis-mysql.PNG" alt="StepLast">
</p>

## Console REDIS 
<p align="center">
  <img src="README-images\redis-console.PNG" alt="StepLast">
</p>



```python
#REDIS DOCKER
docker run --name myredis -p 6379:6379 -d redis:latest

#enter of redis container 
#docker exec -it <ID_o_nombre_del_contenedor> redis-cli
docker exec -it myredis redis-cli

#Get all keys
KEYS *

# Get alls tasks
LRANGE tasks 0 -1

#Comands for use docker container mysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=mypassword -p 3306:3306 -d mysql:latest
#docker exec -it mymysql bash
#mysql -u root -p
#create database flaskmysql;
```

```python
app.config['REDIS_URL'] = 'redis://localhost:6379/0' 
```
The /0 value means that the database space with index 0 is being used on the Redis server. In most typical configurations, Redis instances have at least one database space, and index 0 is commonly used. However, you can specify a different number according to your needs.

El valor /0 significa que se está utilizando el espacio de base de datos con el índice 0 en el servidor Redis. En la mayoría de las configuraciones típicas, las instancias de Redis tienen al menos un espacio de base de datos, y el índice 0 se utiliza comúnmente. Sin embargo, puedes especificar un número diferente según tus necesidades.