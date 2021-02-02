import datetime, time
import meme ,fact
if __name__ == '__main__':
    while 1:
        x = datetime.datetime.now( )
        if x.strftime("%X") == '10:30:15':
            meme.full_run( )
            break
        elif x.strftime("%X")== '22:30:15':
            fact.insta_upload_fact()
            break
        else:
            print(x.strftime("%X"))
            time.sleep(1)
