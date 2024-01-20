# raise Exception mechanism
somthing = 2 
if somthing != 2:
    raise Exception("Failed - somthing is not eaual to 2")
else:
    pass

assert(somthing == 2)

# try & catch mechanism
try:
    with open('Nofile.txt','r') as reader:
        pass
except Exception as e:
    print(e) # not if its **raise Exception
# finally will run no matter if try has failed or not 

finally:
    print("i will run no matter the result @!")