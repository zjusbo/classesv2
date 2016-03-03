#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# 
# This is a demo file illustrating the usage of this tool
from Assignment import Assignment
import re

foldername = "PS4_ Animation, Methods with Return, Simple Conditionals"
def main():

    # set the assinment folder name
    
    # construct assignment object
    assign = Assignment(foldername)
    # set grading function
    assign.setGradeFunc(grade)

    # execute grading function to each submission
    print "Grading " + foldername + "..."
    assign.grade()

    # commit grading to grades.csv file
    print "Commiting " + foldername + "..."
    assign.commit()

    print "Finished! Please upload the result to classesv2."

def grade(submission):
    """grading function
       the function takes 1 parameter which is a dictionary of one student's submitted attachments
       key is attachment filename
       value is attachment absolute path
       grading function should return a tuple containing 2 elements, grade(float) and feedback comment(string)
    """
    return grade_pset4(submission)

def grade_pset4(submission):
    import os
    oldPath = os.getcwd()
    # change working directory

    os.chdir(foldername)
    os.chdir(submission.path)
    os.chdir("Submission attachment(s)")
    # complile
    stdout, stderr = run("javac Cashier.java")
    print(stdout)
    
    # run it
    run_checkout("java Cashier", "1.28 1 6.0 5.00")
    run_checkout("java Cashier", "1 1 0.00 1.00")
    run_checkout("java Cashier", "1.28 1 6.0 1.00")

    print("Name: " + submission.path)
    grade = raw_input("Grade: ")
    comment = raw_input("Comments: ")
    dummyScore = float(grade)
    if grade == -1:
        # re-run current case
        return grade_pset4(submission)
    dummyComment = comment
    os.chdir(oldPath)
    return dummyScore, dummyComment

def run_checkout(command, user_input = ""):
    stdout, stderr = run(command, user_input)
    if stdout != None:
        print(stdout)
    if stderr != None:
        print(stderr)

def run(command, user_input = ""):
    from subprocess import Popen, PIPE
    p = Popen(command, stdin= PIPE, stdout = PIPE) #NOTE: no shell=True here
    print(command + " " + user_input)
    stdout, stderr = p.communicate(user_input)
    p.wait() # wait until it finish
    return stdout, stderr
    
if __name__ == '__main__':
    main()