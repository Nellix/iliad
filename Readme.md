## Traccia

In allegato troverai il documento word ***“TECHNICAL TEST.docx”*** che ti servirà come linea guida.
Dopo aver completato tutto avrò bisogno di ricevere:


**Task 1 (solo il backend, optional frontend):**

 - File zip con dentro la root del progetto (per quanto riguarda il
   testing puoi procedere pure solo a testare le API Backend) e il dump
   del database MySql, Postgres o altro a tua scelta.
 - Il Dockerfile contenente i servizi frontend, backend e database.
 - (Optional) Una delle API riguarda proprio la ricerca di un ordine
   (orders_search). Potresti creare parallelamente una ricerca sui campi
   a tua disposizione utilizzando un ipotetico elasticsearch?
 - (Optional) Una delle API riguarda avere informazioni riguardo un
   determinato ordine (/orders/{order_id}). Potresti spiegarmi che cosa
   utilizzeresti per diminuire il carico sul database? Un sistema di
   caching? O altre soluzioni? 
   Una soluzione sarebbe usare un motore di caching prima del database. In particulare consiglierei Redis come cache del db . Ci sono varie *strategie di caching* :
   - **Read-Through:**
The application code does not explicitly interact with the cache. Instead, the cache provider (Redis) is responsible for loading data into itself when a cache miss occurs.
	- **Cache-Aside** is a caching strategy where the application code is responsible for loading data into the cache.
  

**Task 2, 3 e 4 (Optional):**

File zip con dentro almeno i 3 scripts (javascript, php e python)


python3.9 manage.py makemigrations  
python3.9 manage.py migrate


docker network create ecommerce
docker-compose up