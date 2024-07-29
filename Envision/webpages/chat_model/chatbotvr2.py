#import pyttsx3
#from voicerecognew1 import Speech
import google.generativeai as palm
palm.configure(api_key='AIzaSyBJDtXi7x6LShMZLWUipiz01fnQIN7KLmw')
def chatbot():
    #opening necessary files
    f1=open('dataset_emotions.txt','r')
    f2=open('userlog.txt','a')
    #accessing function from class
    #palm_speech = Speech()

    #setting up palm api
    defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0,
    'candidate_count': 2,
    'top_k': 40,
    'top_p': 0.95,
    }
    context = "Mental health care taker. Give short and comforting words to the user."
    examples = eval(f1.read())
    emo_dict={("feeling overwhelmed","can't handle it anymore","overwhelmed","too much"):["Break tasks into smaller and manageable steps","Prioritize tasks and focus on one thing at a time."],
    ("exhaustion","tiredness","i am tired but i can't sleep"):["Prioritize sleep hygiene","Establish a consistent sleep schedule","create a relaxing bedtime routine","limit screen time before bed."],
    ("changes in Sleep Pattern","can't fall asleep","I'm sleeping too much but still feel tired","insomnia"):["Establish a regular sleep routine", "limit caffeine and screen time before bed","create a comfortable sleep environment."],
    ("i don't enjoy things I used to love","depressed","depression","Loss of Interest"):["Reconnect with activities that used to bring joy","Set small, achievable goals to regain a sense of accomplishment."],
    ("irritability","irritation","irritated"):["Practice stress-management techniques such as deep breathing or meditation","Identify and communicate triggers."],
    ("isolation","feeling isolated","loneliness","lonely"):["Reach out to friends or family","Join social groups or activities."],
    ("negative self-talk","i am useless","i am worthless"):["Challenge negative thoughts with positive affirmations.","Practice self-compassion"],
    ("appetite changed","i am not feeling hungry","i don't eat as i used to"):["Establish regular, balanced meals.","Monitor emotional eating patterns."],
    ("feeling hopeless","hopeless","lost hope"):["Reach out to a trusted friend, family member, or mental health professional.","Focus on setting small, achievable goals."],
    ("increased anxiety","anxious","feeling very anxious"):["Practice relaxation techniques such as deep breathing or mindfulness.","Identify and challenge anxious thoughts."],
    ("I want to cry but its bad to cry",):["What happened? Crying is a way to vent all your feelings out.It is not bad."]}
    messages =['Hey']
    response = palm.chat(
        **defaults,
        context=context,
        examples=examples,
        messages=messages,
    )

    #setting voice of pyttsx3 text to speech converter
    #engine = pyttsx3.init()
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)

    #chatbot implementation
    #a = palm_speech.speak()
    a=input("Hello! How may I help you?\n").lower()
    messages.append(a)
    print('Your message:',a)
    b1 = ['thank you', 'no','nope','bye-bye','tata', 'thanks', 'I am leaving', 'good bye','goodbye','hello', 'greetings', 'hi', 'hey']
    #making sure an input exists
    if a!=None:
        a=a.lower()
        if a in b1:
            if a in ['hello', 'greetings', 'hi', 'hey']:
                response_wc = response.reply("A warm and approachable one line welcome for the user to open up.Be unique")
                b = response_wc.last
                print(b)
                #engine = pyttsx3.init()
                #engine.say(b)
                #engine.runAndWait()
                #continue
            else:
                response1 = response.reply("I am leaving, thank you. Give a motivational send off and ask the user to reach out to you always")
                response_end = response1.last
                f2.write(str(messages))
                print(response_end)
                #engine.say(response_end)
                #engine.runAndWait()
                #break
        else:
            fl=0
            for i in emo_dict:
                for j in i:
                    if j in a:
                        response_convo = response.reply(str(emo_dict[i])+"Don't talk about suicide.Give only 1 idea to tackle the mentioned problem.Don't suggest referring the doctor,therapist,professional help.\
                                                            Enquire if anything else is needed.")
                        b = response_convo.last
                        bwa=''
                        for i in b:
                            if i!='*':
                                bwa+=i
                        print(bwa)
                        #engine.say(bwa)
                        #engine.runAndWait()
                        fl=1
                        break
                if fl==1:
                    break
                
            else:
                if 'no friends' in a:
                    response_convo = response.reply(a+"Only suggest 2 new ideas to keep him happy without friends.Enquire if anything else is needed.")
                    b = response_convo.last
                        
                elif 'who are you' in a:
                    b="I am your safest mental health chatbot Here to make you happy!"
                elif 'how are you' in a:
                    response_convo = response.reply(a+"give just one positive mental health quote")
                    b = response_convo.last
                elif a in ('suicide','suicidal','die','death'):
                    response_convo = response.reply("Tell the user you are there for them despite whatever.Enquire if anything else is needed.Contact suicidal helpline!")
                    b = response_convo.last
                else:
                    response_convo = response.reply(a +"Answer in one line.Give only 1 positive quote.Stop with listing with numbers just 2 activities to do for good mental health from the examples in examples of responses prompt.\
                                                    Don't suggest referring the doctor,therapist,professional help.Enquire if anything else is needed.")
                    b = response_convo.last
                    
                    
                if '*' in b:
                    bwa=''
                    for i in b:
                        if i!='*':
                            bwa+=i
                    print(bwa)
                    #engine.say(bwa)
                    #engine.runAndWait()
                else:
                    print(b)
                    #engine.say(b)
                    #engine.runAndWait()
        return b
    f1.close()
    f2.close()
chatbot()