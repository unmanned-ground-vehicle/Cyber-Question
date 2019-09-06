import base64
"""
Program used to encode the secret message 
"""
def encoder(enc):

    ret = base64.b64encode(enc)
    return ret

if __name__=="__main__":
	
	file = open("secret_message.png","rb")
	info=file.read()
	new = encoder(info)
	new_file=open("encoded.png","wb")

	new_file.write(new)
	new_file.close()
	file.close()
