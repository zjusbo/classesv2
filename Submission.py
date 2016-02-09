#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Bo Song
# Email: bo.song@yale.edu
# Date: 2/8/2016
# 
# TODO: support parsing content of submission, not only attachments.
#       support auto unzip attachments

import os, re



class Submission(object):
    """Submission class for each student's submission
       string - name (name of submission folder,  for example: 'Alnxxx, Mark(abc123)')
       string - netid 
       string - timestamp
       string - comment
       dict - attachments:
            key - attachment name
            value - attachment path
    """
    def __init__(self, name):
        super(Submission, self).__init__()
        self.path = name

        oldPath = os.getcwd()

        # change working directory
        os.chdir(self.path)
        
        # fetch netid
        self.netid = self._parseNetid()
        
        # read timestamp
        self.timestamp = self._parseTimestamp()

        # read attachments
        self.attachments = self._parseAttachments()

        # init comment
        self.comment = ""

        # init grade
        self.grade = 0

        # retrieve working directory 
        os.chdir(oldPath)

    def setComment(self, comment):
        """Write comment"""
        self.comment = str(comment)

    def getTimestamp(self):
        """Read timestamp 
           return - int
        """
        return self.timestamp

    def setGrade(grade):
        """Write grade"""
        self.grade = grade

    def _parseTimestamp(self):
        filename = 'timestamp.txt'
        with open(filename, 'r') as timestampFile:
            timestamp = int(timestampFile.read())
            return timestamp
        # raise exception
        raise FileNotFoundError('File not found: ' + self.path + '/' + filename)

    def _parseNetid(self):
        """Parse netid from folder path"""
        pattern = re.findall("\(.+\)", self.path)
        if pattern:
            # erase surronding parenthesis
            netid = pattern[-1][1:-1]
            return netid
        else:
            raise NameError("Parse netid failed: " + self.path)

    def _parseAttachments(self):
        attachmentFolder = 'Submission attachment(s)'
        os.chdir(attachmentFolder)

        filenames = os.listdir('./')
        attachments = {}

        for name in filenames:
            attachments[name] = os.getcwd() + '/' + name

        # retrieve working directory
        os.chdir('../')
        return attachments

def main():
    foldername = "PS1_ Getting started/Alxxx, Mark(abc123)"
    sub = Submission(foldername)

if __name__ == '__main__':
    main()