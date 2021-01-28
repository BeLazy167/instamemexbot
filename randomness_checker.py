
import os
import random

random_list = []
random_list_full = []
def file_to_list():
    with open( "listofpages.txt", "r" ) as listofpages :
        lines = listofpages.readlines()
    random_list_full_without_n =  [ element.strip() for element in lines ]
    print(random_list_full_without_n)
    random_list = random_list_full_without_n[-6:]
    return random_list
def delete():
    try:
        os.remove( 'temp.jpg' )
        os.remove( 'watermark.jpg' )
        os.remove( 'watermark.jpg.REMOVE_ME' )
    except:
        print('nothing deleted')

def random_check() :
    page_list = [ 'funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                  'SaimanSays/', 'wholesomememes' ]
    to_check = random.choice( page_list )
    random_list = file_to_list( )
    f = open( "listofpages.txt", "a" )
    if len(random_list) < 6 :
        if len( random_list ) == 0 :
            random_list.append( to_check )
            print( random_list )
            to_write = to_check + "\n"
            f.write( to_write )
            return to_check
        else :
            for pages in random_list :
                if pages == to_check :
                    # print('faied')
                    return random_check( )
                else :
                    random_list.append( to_check )
                    print( random_list )
                    to_write = to_check + "\n"
                    f.write( to_write )
                    return to_check
    else :
        t = 0
        for pages in random_list :
            if pages == to_check :
                t = 0
                break
            else :
                t = 1
                continue
        if t == 1 :
            random_list.pop( 0 )
            random_list.append( to_check )
            print( random_list )
            to_write = to_check + "\n"
            f.write( to_write )
            return to_check
        else :
            # print('faied')
            return random_check( )


