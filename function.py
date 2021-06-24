
# sending whatsapp message(only one time face detected)

def whatsapp():
    import os
    import pywhatkit as wt
    
    try:
        phn= input( "Enter the phone number: ")
        wt.sendwhatmsg_instantly("+91"+(phn),"Hi, Message from Ajinkya")
        print("Whatsapp message send successfully")
    
    except:
                    # handling exception
                    # print error
        print("Try once again")
        

        
        
        
# Sending email(only one time face detected)        
        
def mail():
    
    import os
    import smtplib
    from getpass import getpass
    
    text= 'example email to Ajeenkya!!'
    mail= smtplib.SMTP_SSL('smtp.gmail.com',465)
    
    malid= input("Enter the login username: ")
    
    passcode= getpass("Enter the password: ")  
    mail.login(malid,passcode)
    
    mail.sendmail('ajeenkya25.2000@gmail.com','ajeenkya25.2000@gmail.com',text)
    print("Your mail has been sent successfully")
    mail.close()
    

    
    

# if 2 face detected then launched an ec2 instance

def ec2():
    import os
    os.system("aws ec2 run-instances --image-id ami-011c99152163a87ae --instance-type t2.micro --count 1 --subnet-id subnet-d4b15bbf --security-group-ids sg-07e2110b077063e07")
    print(" Instance has been launched successfully !!!")

    
    
    
    
# if 2 face detected then create an 5 gb ebs volume and attach it to the instance

def ebs():
    import os
    os.system("aws ec2 create volume --availability-zone ap-south-1 --size 5 --volume-type gp2")
    print(" Volumes has been created successfully and by default attach to (sda) device ")