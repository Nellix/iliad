##  Explanation
I have implemented the following tasks:

- **task1** backend only + minimal CI pipeline . You can find the code into *task1* branch
- **task2**  You can find the code into *task2* branch
- **task3**  You can find the code into *task3* branch
- **task4**   You can find the code into *task4* branch

In each branch, there is a Readme.md file describing better the solution implmented.


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
Il codice dell'aaplicazione non interagisce esplicitamente con la cache. Invece, è il cache provider (i.e. Redis) il responsabile di caricare i dati dentro di se quando c'è unca cache miss .
	- **Cache-Aside:** Il codice dell'applicazione è responsabile del caricamento dati nella cache. 
    

**Task 2, 3 e 4 (Optional):**

File zip con dentro almeno i 3 scripts (javascript, php e python)


