#!/usr/bin/env python
"""
title: Employee_Task.py
description:
  This is a demo exercise for my job application at Cerri.com
    1, We have a group of employees who can achieve a certain amount of work on a daily basis. We represent this amount of work as task_point (a integer). 
    2, This group of employees needs to complete a list of tasks. The task complexity is also represented by task_point.
    3, The goal of this exercise is to find the best possible way to dispatch tasks between all the employees so that the workload of each employee is as evenly spread as possible.
author: Kai Zhou
version: 1.0
python_version: 2.7.3
"""

import numpy as np
import random as rd

# define some constants for batch testing
MAX_NUM_OF_EMPLOYEE = 100
MAX_NUM_OF_TASK = 200
MAX_EMPLOYEE_TASK_POINT = 30
MAX_TASK_POINT = 80
TEST_ROUNDS = 20

class Employee(object):
    """An employee that has the following properties:

    Attributes:
        nickname: A string representing the employee's name.
        task_point: An integer representing the amount of work this employee can achieve per day.
        assigned_tasks: A list of tasks that are assigned to this employee.
        total_task_points: Total task points that in the assigned_tasks list.
    """
    def __init__(self, task_point, nickname):
        """Return a Employee object whose name is *nickname* and whose task point is *task_point*."""
        self.task_point = task_point
        self.nickname = nickname
        self.assigned_tasks = []
        self.total_task_points = 0

    def assign_task(self, task):
        """Assign the task to this employee, update the total_task_points."""
        self.assigned_tasks.append(task)
        self.total_task_points += task.task_point

    def get_total_task_points(self):
        """Return the total task points for this employee."""
        return self.total_task_points

    def __cmp__(self, other):
        """Override the cmp function for sorting employees by task points."""
        if self.task_point > other.task_point:
            return 1
        elif self.task_point < other.task_point:
            return -1
        else:
            return 0

    def __str__(self):
        """Return the object infomation in a designed format."""
        all_task_print = ''
        for task in self.assigned_tasks:
            all_task_print += str(task) + '\n'
        return '----------------------\n' + 'Employee name: ' + self.nickname + '\n' + 'Employee task point: ' + str(self.task_point) + '\n' + 'List of all tasks assigned to this employee:\n' + all_task_print + 'Total task points assigned to this employee: ' + str(self.get_total_task_points()) + '\n----------------------\n'

class Task(object):
    """A task that has the following properties:

    Attributes:
        name: A string representing the task's name.
        task_point: An integer representing the amount of work this task needs.
    """    
    def __init__(self, task_point, name):
        """Return a Task object whose name is *name* and task point is *task_point*."""
        self.task_point = task_point
        self.name = name

    def __cmp__(self, other):
        """Override the cmp function for sorting tasks by task points."""        
        if self.task_point > other.task_point:
            return 1
        elif self.task_point < other.task_point:
            return -1
        else:
            return 0

    def __str__(self):
        """Return the object infomation in a designed format."""        
        return '\tTask name: ' + self.name + ';\tTask point: ' + str(self.task_point)        


class TaskAssigner(object):
    """A TaskAssigner that manages the task assigning job, it has the following properties:

    Attributes:
        employees: A list of employees.
        tasks: A list of tasks.
    """
    def __init__(self):
        """Return a TaskAssigner object."""        
        self.employees = []
        self.tasks = []
        
    def create_employees(self, task_points, nicknames=[]):
        """Create a list of employee objects from the given task_points list"""
        if nicknames == []:
            # if nicknames are not given, create sequtial names for them
            for i in range(1, len(task_points)+1):
                nicknames.append("Employee_NO." + str(i))
        self.employees = []
        for task_point, nickname in zip(task_points, nicknames):
            self.employees.append(Employee(task_point, nickname))
        # sort the employees in descending order, employees with large task points in the front
        self.employees = sorted(self.employees, reverse=True)

    def create_tasks(self, task_points, names=[]):
        """Create a list of task objects from the given task_points list"""        
        if names == []:
            # if names are not given, create sequtial names for them            
            for i in range(1, len(task_points)+1):
                names.append("Task_NO." + str(i))
        self.tasks = []
        for task_point, name in zip(task_points, names):
            self.tasks.append(Task(task_point, name))
        # sort the tasks in descending order, tasks with large task points in the front            
        self.tasks = sorted(self.tasks, reverse=True)

    def assign_all(self):
        # average_usage: average usage of each employee
        average_usage = sum([task.task_point for task in self.tasks])/float(sum([employee.task_point for employee in self.employees]))
        index_employee, index_task = 0, 0
        # first round, greedy fill each employee from large to small
        while index_employee < len(self.employees) and index_task < len(self.tasks):
            # if current employee is not filled up with tasks, keep filling in
            if self.tasks[index_task].task_point + self.employees[index_employee].get_total_task_points() <= self.employees[index_employee].task_point*average_usage:
                self.employees[index_employee].assign_task(self.tasks[index_task])
                index_task += 1
            # current employee has reached the usage, move to the next employee
            else:
                index_employee += 1
        # second round, sequential fill the remaining tasks
        index_employee = 0
        while index_task < len(self.tasks):
            self.employees[index_employee%len(self.employees)].assign_task(self.tasks[index_task])
            index_task += 1
            index_employee += 1

    def print_all_employee(self):
        """Print the employee infomation."""
        for employee in self.employees:
            print employee

    def print_evaluation_metrics(self):
        """Print the evaluation metircs for the algorithm."""
        workload_array = []
        for employee in self.employees:
            workload_array.append(float(employee.total_task_points)/employee.task_point)
        workload_array = np.array(workload_array)
        print 'The average workload is: ' + str(np.mean(workload_array)) + '\nThe std is: ' + str(np.std(workload_array)) + '\nThe min workload is: ' + str(min(workload_array)) + '\nThe max workload is: ' + str(max(workload_array))
        
    def demo_test(self):
        """Test the algorithm using a demo input."""
        #self.create_employees([1,2,3])
        self.create_employees([1,2,3],['Jim','Mike','John'])
        #self.create_tasks([1,2,3,2,4,11,2,3,2,4,8])
        self.create_tasks([1,2,3,2,4,11,2,3,2,4,8],['Coding','Programming','Hacking','Training','Presentation','Meeting','Write report','Experimenting','Coffeeing','Interviewing', 'Offer'])
        self.assign_all()
        self.print_all_employee()
        self.print_evaluation_metrics()

    def batch_test(self):
        """Batch testing the algorithm using random generated inputs."""
        for i in range(TEST_ROUNDS):
            print '\n---------- testing round: ' + str(i) + ' -------------\n'
            num_of_employees = rd.randint(1,MAX_NUM_OF_EMPLOYEE)
            num_of_tasks = rd.randint(1,MAX_NUM_OF_TASK)
            # generate random employees
            emp_task_points = []
            for n in range(num_of_employees):
                emp_task_points.append(rd.randint(1,MAX_EMPLOYEE_TASK_POINT))
            # generate random tasks
            task_points = []
            for n in range(num_of_tasks):
                task_points.append(rd.randint(1,MAX_TASK_POINT))
            self.create_employees(emp_task_points)
            self.create_tasks(task_points)
            self.assign_all()
            self.print_evaluation_metrics()

if __name__ == "__main__":
    myTaskAssigner = TaskAssigner()
    myTaskAssigner.demo_test()
    #print '+++++++++++++++++++ BEGIN BATCH TESTING ++++++++++++++++++++'
    #myTaskAssigner.batch_test()
