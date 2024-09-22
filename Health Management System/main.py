import time
def exercise(whatyouwanttodo):
    person=int(input("Press 1 for Deepika, 2 for Rohit & 3 for Deep"))
    if(person==1):
        if(whatyouwanttodo==1):
            with open('Deepika_exercise.txt', 'a') as file:
                suggestExercise = str(input('Suggest Exercise'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which diet suggested:" + local_time + "Suggested Exercise:" +  suggestExercise)
        else:
            with open('Deepika_exercise.txt', 'r') as file:
                contents=file.read()
            print(contents)
    elif(person==2):
        if(whatyouwanttodo==1):
            with open('Rohit_exercise.txt', 'a') as file:
                suggestExercise = str(input('Suggest Exercise'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which Exercise suggested:" + local_time + "Suggested Exercise:" +  suggestExercise)
        else:
            with open('Rohit_exercise.txt', 'r') as file:
                contents=file.read()
            print(contents)
    else:
        if(whatyouwanttodo==1):
            with open('Deep_exercise.txt', 'a') as file:
                suggestExercise = str(input('Suggest Exercise'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which Exercise suggested:" + local_time + "Suggested Exercise:" +  suggestExercise)
        else:
            with open('Deep_exercise.txt', 'r') as file:
                contents=file.read()
            print(contents)
        
def diet(whatyouwanttodo):
    person=int(input("Press 1 for Deepika, 2 for Rohit & 3 for Deep"))
    if(person==1):
        if(whatyouwanttodo==1):
            with open('Deepika_diet.txt', 'a') as file:
                suggestDiet = str(input('Suggest diet'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which diet suggested:" + local_time, + "Suggested Diet:" +  suggestDiet)
        else:
            with open('Deepika_diet.txt', 'r') as file:
                contents=file.read()
            print(contents)
    elif(person==2):
        if(whatyouwanttodo==1):
            with open('Rohit_diet.txt', 'a') as file:
                suggestDiet = str(input('Suggest diet'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which diet suggested:" + local_time, + "Suggested Diet:" +  suggestDiet)
        else:
            with open('Rohit_diet.txt', 'r') as file:
                contents=file.read()
            print(contents)
    else:
        if(whatyouwanttodo==1):
            with open('Deep_diet.txt', 'a') as file:
                suggestDiet = str(input('Suggest diet'))
                seconds = time.time()
                local_time = time.ctime(seconds)
                file.write("Time at which diet suggested:" + local_time, + "Suggested Diet:" +  suggestDiet)
        else:
            with open('Deep_diet.txt', 'r') as file:
                contents=file.read()
            print(contents)
     
whatyouwanttodo = int(input("Press 1 for log and 2 for retrieve"))
if(whatyouwanttodo==1):
    activity = input("Press 1 for diet & 2 for exercise")
    if(activity==1):
        diet(whatyouwanttodo)
    else:
        exercise(whatyouwanttodo)
    
else:
    activity = input("Press 1 for diet & 2 for exercise")
    if(activity==1):
        diet(whatyouwanttodo)
    else:
        exercise(whatyouwanttodo)
