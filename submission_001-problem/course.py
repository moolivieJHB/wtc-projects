def mappingfunc(s):
    counter=0
    output=''

    for i in s:
        if counter==0:
            output =output +str(i) +'.'
            counter= counter +1
        elif counter==1:
            output= output + str(i) +'- '
            counter= counter +1
        elif counter==2:
            output= output + str(i) +'- '
            counter = counter+1
        elif counter==3:
            output= output + str(i) 
            counter = counter+1
        elif counter==4:
            output= output + ('[{}]\n'.format(i))
    return output
def create_outline():
    """
    TODO: implement your code here

    """
    topics=['Introduction to Python' , 'Tools of the Trade' ,'How to make decisions'
    , 'How to repeat code' , 'How to structure data' , 'Functions' , 'Modules']
    course_topics=set(topics)
    topicslist=list(course_topics)
    topicslist.sort()
    
    print('Course Topics:')
    for m in range(len(topicslist)):
        print('* ' + topicslist[m])
    
    problems=['Problem 1','Problem 2' ,'Problem 3']
    resultmap={}    #empty map

    print('Problems:')
    for m in  topicslist:
        resultmap[m]=problems  # to print headng problems
        
    for k in (resultmap):
            print('*' , k ,':', ', '.join(resultmap[k]))  # to list each topic
  


        
    print()
    print('Student Progress:')
    student_1=(1 ,'Nyari', 'Introduction to Python' , 'Problem 2 ' , 'STARTED')
    student_2=(2 , 'Adam', 'How to make decisions' , 'Problem 3' , 'GRADED')
    student_3=(3,'Pam','Functions', 'Problem 1' , 'COMPLETED')
    student_4=(4,'Jim', 'How to structure data' , 'Problem 2 ' , 'STARTED')
    student_5=(5 ,'Oscar', 'How to repeat code' , 'Problem 1' , 'GRADED')
    student_6=(6,'Andy','Functions', 'Problem 3' , 'COMPLETED')

    student_list=[student_1 ,student_2 , student_3 ,student_4, student_5 ,student_6]
    order={'STARTED' : 0 , 'GRADED' : 1 , 'COMPLETED' : 2}
    student_list.sort(key= lambda a : order[a[4]])
    student_map=list(map(mappingfunc , student_list))
   

    stud=''.join(student_map)

    print(stud)
    

if __name__ == "__main__":
    create_outline()
