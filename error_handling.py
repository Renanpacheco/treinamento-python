#error handling
array=[1,10]
archive=open('notes.txt', 'r')
try:
    text=archive.read()
    #division=10/0
    #acess=array[3]
    acess=array[1]
    #x=a
except ZeroDivisionError:
    print('it is not possible to divide by zero')
#except BaseException as ex:
    #print('error: {}'.format(ex))
except Exception as ex:
    print('error: {}'.format(ex))
finally:
    print('running file')
    archive.close()