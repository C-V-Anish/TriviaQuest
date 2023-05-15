# TriviaQuest
 A timed Quiz API that enables users to create and participate in quizzes with ease. Features include Quiz Creation, Timed Quizzes, Integration Capabilities.<br>

Salient features of this project include :-<br>
i) The REST API was made using Django REST Framework.<br>
ii) Swagger UI was used for the API's documentation, while the API was deployed on Railway.<br>
iii) JWT Authentication was used for login and accessing the various features of the API, and the endpoints were made as per the requirements.<br>

EndPoints :-<br>
i) POST /quizzes - to create a new quiz.<br>
ii) GET /quizzes/active - to retrieve the active quiz.(the quiz that is currently within its start and end time)<br>
iii) GET /quizzes/:id/result - to retrieve the result of a quiz by its ID.<br>
iv) GET /quizzes/all - to retrieve the all quizes.<br>
