# README #

This README would normally document whatever steps are necessary to get your application up and running.

## Brief ##

About

Company needs internal service for its’ employees which helps them to make a decision
on lunch place. 

Each restaurant will be uploading menus using the system every day over API
Employees will vote for menu before leaving for lunch on mobile app for whom backend has to be implemented
There are users which did not update app to the latest version and backend has to support both versions.
Mobile app always sends build version in headers.

Needed API’s:

- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Voting for restaurant menu (Old version api accepted one menu, New one accepts top three menus with respective points (1 to 3)
- Getting results for current day

Requirements:

Solution should be built using Python and preferably Django Rest Framework, but any other framework works
App should be containerised
Project and API Documentation
• Tests

Extra points
HA Cloud Architecture Schema/Diagram (Preferably Azure)
Usage of Linting and Static typing  tools


### API Schemas ###

* [Redoc](http://localhost:8000/api/v1/schema/redoc/)
* [Swagger](http://127.0.0.1:8000/api/v1/schema/swagger-ui/)
