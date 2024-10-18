# Task-Tracker
This is a roadmap.sh test to creating a task tracker

# To run the code

You need to install python 3.10.10 or greater. and open the cmd in the directory of where the files are stored

## link
https://roadmap.sh/projects/task-tracker

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

* Add, Update, and Delete tasks
* Mark a task as in progress or done
* List all tasks
* List all tasks that are done
* List all tasks that are not done
* List all tasks that are in progress
* Here are some constraints to guide the implementation:

    You should use Python to build this project.
    Use positional arguments in command line to accept user inputs.
    Use a JSON file to store the tasks in the current directory.
    The JSON file should be created if it does not exist.
    Use the native file system module of your programming language to interact with the JSON file.
    Do not use any external libraries or frameworks to build this project.
    Ensure to handle errors and edge cases gracefully.


# Example
The list of commands and their usage is given below:

## Adding a new task
> pyhton main.py add "Buy groceries"
### Output: Task added successfully (ID: 1)

## Updating and deleting tasks
> pyhton main.py update 1 "Buy groceries and cook dinner"
> pyhton main.py delete 1

## Marking a task as in progress or done
> pyhton main.py mark-in-progress 1
> pyhton main.py mark-done 1

## Listing all tasks
> pyhton main.py list

## Listing tasks by status
> pyhton main.py list done
> pyhton main.py list todo
> pyhton main.py list in-progress

# Task Properties
Each task should have the following properties:

**id**: A unique identifier for the task
**description**: A short description of the task
**status**: The status of the task (todo, in-progress, done)
**createdAt**: The date and time when the task was created
**updatedAt**: The date and time when the task was last updated


**NB** Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.
