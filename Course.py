#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Bo Song  http://www.bo-song.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#  
# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# NOT FINISHED

# TODO: retrieve assign list, download submissions package
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

	def retrieveAssignList(self):
		pass

	def downloadAssign(self, name):
		pass