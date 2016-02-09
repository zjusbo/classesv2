# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# 
# NOT FINISHED!
# This class should complete login, logout, retrieve course list function

class Classesv2(object):
	"""docstring for Classesv2"""
	def __init__(self):
		super(Classesv2, self).__init__()
		
		# classesv2 base url
		self.baseurl = "https://classesv2.yale.edu/"
		
		# courses object dict
		self.courses = {}

	def login(self, username, password):
		pass

	def logout(self):
		pass