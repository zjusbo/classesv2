#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# 

class Course(object):
	"""Course class"""
	def __init__(self, courseCode):
		super(Course, self).__init__()
		
		# set course code
		self.courseCode = courseCode
		
		# set course name
		self.courseName = ""

		self.assignments = {}


	def setCourseName(self, name):
		self.courseName = name
