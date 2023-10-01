## TASK 1

**Knowledge**:

PHP Lumen/Laravel 7.x/8.x or **Python Django REST Framework**/FastAPI (backend)
Vuejs/JQuery (frontend)
Bootstrap
**Database - mysql**

### Assumptions

 
- The XXX team wants to have an overview of the orders placed during the current day on the e-commerce.
- You know that the ecommerce platform exposes useful API.
- You don’t know the URL of that API and how you can authenticate
- You know the format of the response
- You can start mocking up the software  

You have to:

1) Consume the API endpoint and manage the response
2) Persists the data on a database
3) Create a simple interface to show the data


**POST**

*/orders_search*  Search orders

**GET**

*/orders/{order_id}* Get a specific order


-   Submission rules are specified for each task.
-   Each task file should properly run and output the correct results.
-   code style, code tidiness, comments are a plus.


##  Explanation
For **Task1** has been implemented only the backend part using Django framework.
Furthermore, a **CI pipeline** has been developed for :
- *building and push docker image* for backend
- *testing django APIs* via django framework

The pipelines is triggered each time new code on the task1 branch is pushed.

### How to run ?
You can run the application via docker-compose by following command in the root directory:

	docker-compose up
The you can use postman collections (in the postman folder), in order to execute apis .

The docker-compose is composed by 3 containers :
- **mysql** mysql db
- **init-backend** for db initization
- **ecommerce-backend** exposing apis on port 8000