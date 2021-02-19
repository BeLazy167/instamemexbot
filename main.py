import datetime, time
import meme, fact

if __name__ == '__main__':
    while 1:
        x = datetime.datetime.now()
        true_time = x.strftime("%X")
        if true_time == '10:31:00':
            meme.full_run()
            break
        elif true_time == '22:31:00':
            fact.insta_upload_fact()
            break
        elif true_time == '22:35:00' or true_time == '10:35:00':
            break
        else:
            print(true_time)
            time.sleep(1)
