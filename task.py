# -*- coding: utf-8 -*-
import urllib2

class Task():

    def __init__(self,task):
        self.task=task
        pass

    def clearFile(self,filename):
        f = open(filename.replace("\n", ""), "w").close()

        pass

    def writeResult(self,res,filename):
        f= open(filename.replace("\n",""),"a")
        if len(res)>0:
            '''f.write("URL: "+self.task[0]+"\n")
            f.write("From: "+str(self.task[1])+"\n")
            f.write("To: "+str(self.task[2])+"\n")'''
            f.write(res)
            f.write("\n\n\n")
        else:
            '''f.write("URL: " + self.task[0] + "\n")
            f.write("From: " + "\n")
            f.write("To: " +  "\n")'''
            f.write(unicode(res,"utf-8"))
            f.write("\n\n\n")
        f.close()
        pass

    def clearResult(self,res,iskl):
        newRes=res;
        for i in iskl:
            newRes=newRes.replace(i,"")
        return newRes
        pass

    def getHtml(self):
        url=self.task[0]

        try:
            response = urllib2.urlopen(url)
            html = response.read();
            self.clearFile(self.task[5])

            if (html.find(self.task[3]) != -1):

                for i in range(len(self.task[1])):
                    startIndex = html.find(self.task[1][i])
                    finishIndex = html.find(self.task[2][i]) + len(self.task[2][i])
                    print str(startIndex) + " " + str(finishIndex)
                    result = html[startIndex:finishIndex]
                    result=self.clearResult(result,self.task[4])
                    self.writeResult(result,self.task[5])
            else :self.writeResult("",self.task[5])
        except:
                self.writeResult("",self.task[5])

        pass

Task