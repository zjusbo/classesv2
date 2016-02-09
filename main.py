from Assignment import Assignment
import re

def main():
	foldername = "PS1_ Getting started"
	assign = Assignment(foldername)
	for key, sub in assign.submissions.iteritems():
		for attachName, attachPath in sub.attachments.iteritems():
			if attachName == 'Self.java':
				with open(attachPath, 'r') as attachFile:
					content = attachFile.read()
					match = re.search('[bB]ook: ?(.+)"', content)
					if match:
						print match.group(1)

if __name__ == '__main__':
	main()