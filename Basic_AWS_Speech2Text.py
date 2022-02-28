#Basic use AWS Boto3 Python package to use AWS Polly for Speech2Text

import boto3

#Explicit Client Coniguration

polly = boto3.client('polly',
                     region_name='us-west-2',
                     aws_access_key_id='<Enter_Your_AWS_Access_Key>',
                     aws_secret_access_key='<Enter_Your_AWS_Secret_Access_Key'

)

result = polly.synthesize_speech(Text='Hello world!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')
                                 
#Save the Audio from the response
audio = result['AudioStream'].read()
with open('helloworld.mp3', 'wb') as file:
    file.write(audio)
