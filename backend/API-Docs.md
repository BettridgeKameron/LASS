# LASS API Documentation
### Notes
If you find a better way of naming something, combining endpoint, follow best practices, etc, please do so! This is only an OUTLINE, and may not be 100% the best way of doing this. Also note, if the given Response/request body doesn't make sense for the endpoint and how you are approaching it __please change this as well__, this is only a __guidline__, and not something to follow 100%. Chances are this will change.

### Note about Asynchronous Design:
The `/api/v1/authorship/writeprint` endpoint gives an example on how we will handle any endpoint where the backend needs a lot of time (more than 10 seconds consistently probably). We will probably handle them asynchronously, where we will give a jobId that they check on the progress. Another approach is to offer webhooks where we will send a notification when it is done processing to a given webhook. **Just because an endpoint currently has or does not have this Asynchronous style, doesn't mean we will or won't make it asynchronous**. It all depends on the algorithm, however just focus on the logic currently, and then we can split into an asynchronous design where needed.

## Authentication

`POST /api/v1/authenticate`
- **Description**: Authenticate users and issue a JWT token for secured endpoints.
- **Request Body**: `{"username": "user", "password": "pass"}`
- **Response**: `{"token": "JWT_TOKEN"}`
- **Note**: [Here is an article on JWT Authentication in Flask](https://www.loginradius.com/blog/engineering/guest-post/securing-flask-api-with-jwt/), but for now you don't necessarily need authentication, as we want something working, but if you don't include it, we will need to later when it is live! 

## Authorship Attribution

`POST /api/v1/authorship/writeprint`
- **Description**: Submit text to generate a unique stylometric writeprint.
- **Request Body**: `{"text": "Sample text here..."}`
- **Response**: `{"jobId": "unique_job_id"}`
- **Notes**: This assumes that creating a writeprint may take some time, to make it asynchronous. But if its fairly quick ( under a few seconds! ), then we can combine this and the next one.

`GET /api/v1/authorship/writeprint/{jobId}`
- **Description**: Retrieve the results of the stylometric analysis using the provided job ID.
- **Response**: `{"writeprint": {...}}`

## Text Rephrasing

`POST /api/v1/text/rephrase`
- **Description**: Rephrase the submitted text to alter wording but keep the same meaning.
- **Request Body**: `{"text": "Original text to rephrase...","writeprint":"Writeprint ID To rephrase like."}`
- **Response**: `{"rephrasedText": "Rephrased version of the text..."}`

## Stylometric Obfuscation

`POST /api/v1/text/obfuscate`
- **Description**: Modify text to anonymize stylometric properties.
- **Request Body**: `{"text": "Text for stylometric obfuscation..."}`
- **Response**: `{"obfuscatedText": "Text after obfuscation..."}`

## Sentiment Analysis

`POST /api/v1/text/sentiment-analysis`
- **Description**: Analyze the sentiment of the provided text.
- **Request Body**: `{"text": "Text to analyze sentiment..."}`
- **Response**: `{"sentimentScore": {...}}`

## User Attributes Prediction

`POST /api/v1/text/predict-user-attributes`
- **Description**: Predict any possible user attributes, ranging from geolocation, gender, age, etc.
- **Request Body**: `{"text": "Text for attributes prediction..."}`
- **Response**: `{"possibleUserInfo": {...}}`

## System Health Check

`GET /api/v1/health`
- **Description**: Check the health and availability of the API service.
- **Response**: `{"status": "healthy"}`

## Further Notes
Be prepared for possible changes in design as we continue (make your code modular, which you should be doing anyways!)

---

Each request to secured endpoints must include the `Authorization` header with the JWT token obtained from `/api/v1/authenticate`.

All endpoints return a `200 OK` status code on success, appropriate error status codes on failure, and a JSON-formatted body.