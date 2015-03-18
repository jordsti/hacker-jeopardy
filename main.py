import webservice
import sys
import jeopardy
if __name__ == '__main__':


    gd = jeopardy.game_data()
    gd.read_file("game1.txt")


    port = 8080
    files_dir = "./"

    ai = 0
    argc = len(sys.argv)
    while ai < argc:
        arg = sys.argv[ai]
        if arg == 'port':
            if ai + 1 < argc:
                ai += 1
                port = int(sys.argv[ai])
        elif arg == 'dir':
            if ai + 1 < argc:
                ai += 1
                files_dir = sys.argv[ai]
        ai += 1

    web_server = webservice.service_thread(port)
    web_server.httpd.files_dir = files_dir
    web_server.httpd.game_data = gd
    web_server.start()

