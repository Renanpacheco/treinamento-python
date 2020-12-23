# working with files

def create_file(name_file):
    archive=open(name_file,'w')
    archive.write('')
    archive.close()

def write_file_directory(text):
    directory='D:/softwares/teste.txt'
    archive=open(directory,'w')
    archive.write(text)
    archive.close()

'''
def write_file(name_file,text):
    archive=open(name_file,'w')
    archive.write(text)
    archive.close()
'''

def update_file(name_file,text):
    archive=open(name_file,'a')
    archive.write(text)
    archive.close()

def read_file(name_file):
    archive=open(name_file,'r')
    text=archive.read()
    print(text)
    archive.close()

def grade_avarage(name_file):
    #students=[]
    archive=open(name_file,'r')
    student_notes=archive.read()
    archive.close()
    student_notes=student_notes.split('\n')
    #print(student_notes)
    for i in student_notes:
        list_notes=i.split(',')
        student=list_notes[0]
        list_notes.pop(0)
        print(student)
        print(list_notes)
        mean= lambda notes: sum([int(j) for j in notes])/4
        print(mean(list_notes))
    #print(students)

if __name__ == "__main__":
    
    archive=input('please enter the file name: ')+'.txt'
    create_file(archive)
    text=input("please enter the text: ")+'\n'
    update_file(archive,text)
    text=input("please enter the text: ")
    update_file(archive,text)
    read_file(archive)
    
    write_file_directory('test')
    
    notes='notes.txt'
    grade_avarage(notes)