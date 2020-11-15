from twilio.rest import Client 

 
account_sid = 'AC4887943c51b0899df889542d2bf46341' 
auth_token = 'xxxxx' 
client = Client(account_sid, auth_token) 
text_val = input("Enter your text to send: ")

def send_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=text_val,      
                              to='whatsapp:+918553225589' 
                          ) 
 
    print(message.sid)
