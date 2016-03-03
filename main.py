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

# set the assinment folder name
foldername = "PS4_ Animation, Methods with Return, Simple Conditionals"

def main():

    
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
    return grade_pset4_part1(submission)


def grade_pset4_part1(submission):
    import os
    from shutil import copyfile
    oldPath = os.getcwd()
    # change working directory
    os.chdir(foldername)
    os.chdir(submission.path)
    os.chdir("Submission attachment(s)")
    
    #copy dependencies
    copyfile(oldPath + "/" + foldername + "/1.png", os.getcwd() + "/1.png")
    copyfile(oldPath + "/" + foldername + "/1.wav", os.getcwd() + "/1.wav")

    # complile, print to console
    run_checkout("javac Animation.java")
    
    # run program, print to console
    run_checkout("java Animation", ["800 600 ","0 0 10 45 ","../../1.png ","800 300 30 -180 ","../../1.wav ","3"])

    while True:
        try:
            print("Name: " + submission.path)
            grade = raw_input("Grade: ")
            # re-run current case, if grade is -1
            if grade == "rerun":
                os.chdir(oldPath)
                return grade_pset4_part1(submission)
            # re-run without user input
            elif grade == "noinput":
                run("java Animation")
                continue
            grade = float(grade)
            comment = raw_input("Comments: ")
        except Exception, e:
            print("Please enter a float for grade")
            print("or enter 'rerun' or 'noinput' ")
        else:
            break
    os.chdir(oldPath)
    return grade, comment

def grade_pset4_part2(submission):
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

    while True:
        try:
            print("Name: " + submission.path)
            grade = raw_input("Grade: ")
            grade = float(grade)
            if abs(grade - (-1)) < 0.1:
                # re-run current case, if grade is -1
                os.chdir(oldPath)
                return grade_pset4(submission)
            comment = raw_input("Comments: ")
        except Exception, e:
            print("Please enter a float grade")
        else:
            break
    os.chdir(oldPath)
    return grade, comment

def run_checkout(command, user_input = None):
    stdout, stderr = run(command, user_input)
    if stdout != None:
        print(stdout)
    if stderr != None:
        print(stderr)

def run(command, user_input = None):
    from subprocess import Popen, PIPE
    import os
    print(os.getcwd())
    if user_input == None:
        # no user_input, read from stdin
        p = Popen(command, stdin = None, stdout = None) #NOTE: no shell=True here
    else:
        # read user_input from PIPE
        p = Popen(command, stdin= PIPE, stdout = PIPE) #NOTE: no shell=True here
    
    if isinstance(user_input, list):
        user_input = "".join(user_input) # convert list to string
    
    print(command)
    print(user_input)
    stdout, stderr = p.communicate(user_input) 
    p.wait() # wait until it finish
    return stdout, stderr
    
if __name__ == '__main__':
    main()