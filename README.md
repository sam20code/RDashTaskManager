# RDashTaskManager

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
