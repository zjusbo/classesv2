#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# 
import os
from Submission import Submission

class Assignment(object):
	"""Assignment class
	   string - name - downloaded assignment folder name
	   dict of Submission objects - submissions - students' submissions:
	   		key - netid
	   		value - submission object
	"""
	def __init__(self, name):
		super(Assignment, self).__init__()
		
		# set assign folder name
		self.path = name

		# change working directory
		oldPath = os.getcwd()
		os.chdir(name)

		# get student submissions
		self.submissions = self._getSubmissions()

		# init deadline timestamp
		self.ddlTimestamp = 0

		# init grade function
		self.gradeFunc = self._dummyGradeFunc

		# retrieve working directory
		os.chdir(oldPath)

	def setDDLTimestamp(self, timestamp):
		self.ddlTimestamp = int(timestamp)

	def setGradeFunc(self, func):
		"""set grading function
		   the function should take 1 parameter which is a dictionary of one student's submitted attachments
		   key is attachment filename
		   value is attachment absolute path
		   grading function should return a tuple containing 2 elements, grade(float) and comment(string)
		"""
		self.gradeFunc = func

	def grade(self):
		"""grade the submissions
		   currently we only grade on attachments of submission
		"""
		for submission in self.submissions.itervalues():
			score, comment = self.gradeFunc(submission.attachments)
			submission.setGrade(score)
			submission.setComment(comment)

	def commit(self):
		"""commit grade information to grade.csv"""
		pass

	def _getSubmissions(self):
		filenames = os.listdir('./')
		submissions = {}
		for filename in filenames:
			# we only focus on directory
			if not os.path.isdir(filename):
				continue
			sub = Submission(filename)
			netid = sub.netid
			submissions[netid] = sub
		return submissions

	def _dummyGradeFunc(self):
		raise NotImplementedError('setGradeFunc(func) should be called before running grade()')

