import datetime, time
import meme ,fact
if __name__ == '__main__':
    while 1:
        x = datetime.datetime.now( )
        if x.strftime("%X") == '10:31:00':
            meme.full_run( )
            break
        elif x.strftime("%X")== '22:31:00':
            fact.insta_upload_fact()
            break
        elif x.strftime("%X")== '22:35:00' or x.strftime("%X")=='10:35:00':
            break
        else:
            print(x.strftime("%X"))
            time.sleep(1)
