# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:17:05 2019

@author: Administrator
"""
import sqlite3
class myDB():
    
    
      def __init__(self, connstr):
          self.myConn = sqlite3.connect(connstr)
          
          
      def getSQLresult(self, sqlstr):
          resultset = self.myConn.execute(sqlstr).fetchall()
          return resultset
    
      def execSQLcommand(self, sqlstr):
          
          
          try:
            myCursor = self.myConn.execute(sqlstr)
            self.myConn.commit()
            print("指令已成功執行:" + sqlstr)
            return myCursor
          except Exception as ex:
            print("指令有誤:", sqlstr, ex)

      def Qo(self, instr):
          return "'" + instr + "'"    