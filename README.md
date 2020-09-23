# The Debugger System
##### Debugger app made using Flask

*In order to view the app in live mode go to https://thedebugger.herokuapp.com/*

To get the full experience login as a Project Manager role

***username : expert***

***password : expert***

## About
Bug Tracker is an application to track errors in software. It was created by Mukammed Alimbet as a student project for the UCLA Extension certificate program in "Application Programming". Bug Tracker uses a ticketing system to record bugs or other issues in the software development process on a per-project basis. It implements user- and role-level security to ensure only authorized users can access tickets and projects. The application was built using Python / Flask framework with an sqlite3 database. Bug Tracker’s webpages use HTML5/Bootstrap. Roles: Bug Tracker has three roles that users can be assigned to. Users are automatically placed in a developer role upon registration. Below are brief descriptions of the permissions of each role:

## Features/Roles

##### Developer:
View tickets for they are assigned to, can add comments or attachments to tickets they have access to.


##### Project Manager:
Create new projects and new tickets and assign users to projects assign a developer to a ticket, can add comments or attachments to tickets.

##### Admin:
Assign users to roles View and edit all tickets Create new projects Assign users to projects For each role, users can add comments or attachments to tickets they have access to.

##### Ticket priorities:
A ticket can be Critical, High, Medium or Low priority.

##### Ticket statuses: 
A ticket can be in one of five statuses:
Open: Ticket automatically assigned this status on creation
Pending: Work on the ticket has been suspended
Resolved: The issue raised in the ticket has been resolved
Closed: All the resolved tickets
Ticket priorities: 
High, Medium, Low
