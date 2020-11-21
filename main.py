#!/usr/bin/env python

import os
import time
from classes import Topic, Subtopic

subtopics = {}
topics = 0
topic_name = ""
topic_names = []

def menu():
    '''
    Shows the mainmenu and gets called every time a action is completed! 
    '''
    print("#"*50 + "\n")
    print(topic_name)
    for key, value in subtopics.items():
        print("--" + key)
        for k, v in value.items():
            for i in v:
               if len(i) > 1:    
                   print("----" + i)
    print("\n" + "#"*50 + "\n")
    print("These are ths topics that already exist: " + ", ".join(topic_names))
    print("What do you want to do?")
    print("(1) Set topic. (2) Add Subtopic with Points. (3) Delete Subtopic with Points. (4) Load Topic. (5) Delete Topic. (6) Save. (7) Exit.")
    
    try:
        choice = int(input(""))
        if choice == 1:
            set_topic()
            menu()
        elif choice == 2:
            if topics != 0:
                add_subtopic() 
                menu()
            else:
                print("First you have to define a topic!")
                menu()
        elif choice == 3:
            if topics != 0:
                delete_subtopic()
                menu()
            else:
                print("First you have to define a topic!")
                menu()
        elif choice == 4:
            load_data()
            menu()
        elif choice == 5:
            delete_topic()
            read_topics()
            menu()
        elif choice == 6:
            save_exit()
            read_topics()
            menu()
        elif choice == 7:
            return
        return 
    except Exception:
        print(f"[Error]  Not a valid option!")
        time.sleep(1)
        os.system("clear")
        menu() 

def set_name():
    name = input("Whats the name of the topic?  ")
    return name

def set_topic():
    global topics
    if topics == 0:
        main_topic = set_name()
    
        global topic, topic_name
        topic = Topic(main_topic)
        topics += 1
        topic_name = topic.name
        os.system("clear") 
    else: 
         print(f'Theres already a topic defined. {topic.name}')
         time.sleep(3)
         os.system("clear")

def add_subtopic():
    global subtopic, dicti, subtopics
    points = []
    name = set_name()
    numberofpoints = int(input("How many points? "))
    
    subtopic = Subtopic(name)
    for i in range(numberofpoints):
        point = input("Whats the " + str(i+1) + ".Point you want to add?  ")
        points.append(point)

    dicti = {
        "name": subtopic.name,
        "points": points
    }
    subtopics[subtopic.name] = dicti
    os.system("clear")

def save_exit():
    global subtopics, topic_name
    if topic_name != "" and topic_name not in topic_names:
        content =  str(subtopics)
        path = topic_name + ".txt"
        f = open(path, "w")
        f.write(content)
        f.close
        topic_name_white = topic_name + " "
        r = open("topics.txt", "a")
        r.write(topic_name_white)
        r.close
        
        topic_name = ""
        subtopics = {}
        topics = 0
        os.system("clear")
        return
    else: 
        os.system("clear")
        return

def delete_topic():
    global subtopics, topic_name, topics
    whatdata = input("What entry do you want to delete?  ")
    path = whatdata + ".txt"
    os.system("rm -r " + path)
    
    f = open("topics.txt", "r")
    data = f.read()
    f.close()
    data_list = data.split(" ")
    for i in data_list:
        if i == whatdata or i == "":
            data_list.remove(i)
            topic_names.remove(i)
    f = open("topics.txt", "w")
    f.write(" ".join(data_list))
    f.close()
    
    topic_name = ""
    subtopics = {}
<<<<<<< HEAD
    topics -= 1
    print(topics)
    time.sleep(5)
=======
    topics = 0
>>>>>>> fb1ad940eeb508a75db85dbc244a1de20aee09ce
    os.system("clear")
    return

def read_topics():
    f = open("topics.txt", "r")
    alltopics = f.read()
    f.close()
    for i in alltopics.split(" "):
        if i != "" and i not in topic_names:
            topic_names.append(i)
    return topic_names

def delete_subtopic():
    global subtopics, topic_name
    if topic_name != "":
        del_subtopic = input("Which subtopic do you want to delete?  ")
        for key, value in subtopics.items():
            if key == del_subtopic:   
                subtopics.pop(del_subtopic)

def load_data():
    global subtopics, topic_name, topics
    whatdata = input("Which Topic do you want to load?  ")
    path = whatdata + ".txt"
    f = open(path, "r")
    data = f.read()
    f.close()
    
    topics += 1 
    dictionary = eval(data) 
    os.system("clear")
    subtopics = dictionary
    topic_name = whatdata 
    topic_names.remove(topic_name)                
    

os.system("clear")  
read_topics()
menu()
