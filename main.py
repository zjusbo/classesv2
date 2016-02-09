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

def main():

	# set the assinment folder name
	foldername = "PS1_ Getting started"
	
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

def grade(attachment_dict):
	"""grading function
	   the function takes 1 parameter which is a dictionary of one student's submitted attachments
	   key is attachment filename
	   value is attachment absolute path
	   grading function should return a tuple containing 2 elements, grade(float) and feedback comment(string)
	"""
	for name, path in attachment_dict.iteritems():
		if name == 'Self.java':
			with open(path, 'r') as attachFile:
					# do some work here
					pass

	dummyScore = 99.0
	dummyComment = "Good Job!"
	return dummyScore, dummyComment

if __name__ == '__main__':
	main()