import datetime, time
import meme ,fact
if __name__ == '__main__':
    while 1:
        x = datetime.datetime.now( )
        if x.strftime("%X") == '13:17:30':
            meme.full_run( )
            break
        elif x.strftime("%X")== '22:30:30':
            fact.insta_upload_fact()
            break
        else:
            print(x.strftime("%X"))
            time.sleep(1)
