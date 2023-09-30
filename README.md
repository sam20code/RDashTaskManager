# RDashTaskManager
** refer project snippet at bottom of page

## Situation:
---
- We are tasked with developing a task management system that enhances team productivity.
- The system must allow users to create, assign, and track tasks efficiently.
- There's a need for flexibility in task management, especially when dealing with potential blockers.
## Task:

- Create a backend system for the task manager.
- Implement a subset of features including task creation, assignment, and filtering.
- Develop an email notification system for task assignments.
## Action (Key Features):

`User Authentication and Role-Based Access:`
- Users must log in as either "admin" or "user."
- Admins have the authority to create sprints.
`Sprint-Based Task Management:`
- Admins can create sprints with unique names, assign creators, set data points, and define sprint dates.
- Instead of traditional due dates, the system utilizes sprints for task management.
`Task Creation and Point Assignment:`
- Users can create tasks within a sprint and assign points to each task.
- Points reflect the estimated effort or complexity of each task.
- This approach offers flexibility for task prioritization.
`User Task Management:`
- Regular users can select a sprint to view tasks they've created within that sprint.
- If users haven't created any tasks, they have the option to add tasks via the navbar.
`Email Notifications (Simulated):`
- Implement a basic email notification system.
- Users receive notifications when tasks are assigned to them, even though actual email sending is not set up.
## Result:
- The developed system provides an effective solution for task management.
- Admins can create sprints and organize tasks within them.
- Users have the flexibility to prioritize tasks within sprints based on their complexity.
- Email notifications, while simulated, enhance user communication.
- The system enhances team productivity by offering a more adaptable approach to task management.

## Detail description
`User Authentication:`
The application offers secure user authentication, allowing both regular users and administrators to create accounts and log in.
Users have different levels of access and permissions based on their roles.
`2. User Home Page:`
Upon logging in, regular users are directed to their personal homepages.
The user homepage presents a list of sprints they are associated with or have access to.
![UserLogin](https://github.com/sam20code/RDashTaskManager/assets/56734174/354387a8-58ee-4af1-98d6-579b9157fc6a)
![userPage](https://github.com/sam20code/RDashTaskManager/assets/56734174/d5c091c1-c3b0-454a-829c-eb6df3fb2405)

`3. Admin Home Page:`
- Administrators have a dedicated homepage.
- The admin homepage displays a comprehensive list of all sprints and tasks created by them.
![admingSignUp](https://github.com/sam20code/RDashTaskManager/assets/56734174/27a5d6d0-07c0-4297-b7ce-446cfb75ff48)
![AdmingPage](https://github.com/sam20code/RDashTaskManager/assets/56734174/a8f2cf14-5c32-4ba1-b833-4c3b97aa7bf3)
`4. Sprint Management:`
- Administrators can create sprints, each with essential attributes like name, creator, data points, and date.
- Administrators have the privilege to edit or update sprint details.
- Users can access and view sprint details.
![AddingSprintForm](https://github.com/sam20code/RDashTaskManager/assets/56734174/c48e61c2-1294-472c-af20-d3309c1434a5)

`5. Task Management:`
- Users can efficiently create tasks linked to specific sprints.
- Tasks are detailed with attributes such as name, description, assignee, points, and state.
- Users and administrators can view and modify task information.
- Tasks are closely associated with specific sprints for effective tracking.
![AddingTaskForm](https://github.com/sam20code/RDashTaskManager/assets/56734174/23cc7bf8-4047-46b3-82cc-c7058793f239)
`6. Task Board:`


- Users can access task boards that are tailored to each sprint.
- Task boards provide a comprehensive view of all tasks associated with a particular sprint.
- Users can easily access and review task details, including name, description, assignee, points, and state.
- A visual indicator displays the total data points allocated for the sprint, ensuring that users stay within set limits.
![UserTaskBoard](https://github.com/sam20code/RDashTaskManager/assets/56734174/edd5f6b0-d4ea-4fe0-b166-f076849ef07e)
`7. HTML Templates and Styling:`
- The application utilizes HTML templates to render dynamic content, providing an intuitive and user-friendly interface.
- CSS styles, possibly with the assistance of Bootstrap, are applied to enhance the visual appeal and layout of the application.

`8. Forms and Models:`
- Django forms facilitate user input, data validation, and interaction with the application.
- Django models define the database structure, governing the storage and retrieval of sprint and task data.

`9. URL Routing and Views:`
- URL patterns are clearly defined to map specific URLs to appropriate views.
- Views handle user interactions and database operations, ultimately rendering the correct HTML templates.
  
`10. Security Measures:`
- Robust security measures are implemented, including Django's built-in CSRF protection and user authentication, to safeguard the application from vulnerabilities.


----
