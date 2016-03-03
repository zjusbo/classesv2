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
	   ddlTimestamp - int - deadline timestamp
	   latePenaltyRate - float - penalty rate for late submission. 0.0(no score)~1.0(no penalty)
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

		# init late penalty rate
		self.latePenaltyRate = 1.0

		# retrieve working directory
		os.chdir(oldPath)

	def setDDLTimestamp(self, timestamp):
		self.ddlTimestamp = int(timestamp)

	def setLatePenalty(self, rate):
		"""percentage of score that a late submission will get.
		   float - rate - 0.0~1.0
		   1.0 means no late penalty
		"""
		self.latePenaltyRate = rate

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
		   currently we only grade for attachments in submission
		"""
		for submission in self.submissions.itervalues():
			score, comment = self.gradeFunc(submission)
			
			# late submission penalty
			if self.ddlTimestamp != 0 and submission.getTimestamp() > self.ddlTimestamp:
				score = score * self.latePenaltyRate
			if score:
				submission.setGrade(score)
			if comment:
				submission.setComment(comment)
			# commit after each grade
			self.commit()

	def commit(self):
		"""commit grade result to grades.csv
		   commit comment to corresponding comment.txt
		"""
		import csv
		# change working directory
		oldPath = os.getcwd()
		os.chdir(self.path)

		gradeFilename = "grades.csv"
		commentFilename = "comments.txt"
		# commit to grade.csv
		output = []
		with open(gradeFilename, 'rb') as csvFile:
			reader = csv.reader(csvFile, delimiter = ',', quotechar = '"')
			for idx, row in enumerate(reader): 
				# we only process body while ignore header
				if idx > 2:
					netid = row[1]
					# get corresponding grade
					if self.submissions.has_key(netid):
						grade = self.submissions[netid].grade
					else:
						# no submission, no score
						grade = 0
					# store string
					grade = str(grade)
					# grade column already exist
					if len(row) > 4:
						row[4] = grade
					else:
						row.append(grade)
				output.append(row)

		# overwrite grades.csv
		with open(gradeFilename, 'wb') as csvFile:
			writer = csv.writer(csvFile, delimiter = ',', quotechar = '"')
			for row in output:
				writer.writerow(row)

		# commit to corresponding comment.txt
		prevPath = os.getcwd()
		for netid, submission in self.submissions.iteritems():
			os.chdir(submission.path)
			with open(commentFilename, 'wb') as txtFile:
				txtFile.write(submission.comment)
			os.chdir(prevPath)


		# retrieve working directory
		os.chdir(oldPath)

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

