import webservice
import sys
import jeopardy
if __name__ == '__main__':

    gd = jeopardy.game_data()
    game_file = None
    port = 8080
    files_dir = "./"

    ai = 0
    argc = len(sys.argv)
    while ai < argc:
        arg = sys.argv[ai]
        if arg == '-port':
            if ai + 1 < argc:
                ai += 1
                port = int(sys.argv[ai])
        elif arg == '-dir':
            if ai + 1 < argc:
                ai += 1
                files_dir = sys.argv[ai]
        elif arg == '-game':
            if ai + 1 < argc:
                ai += 1
                game_file = sys.argv[ai]
        ai += 1

    if game_file is None:
        print("Please specify a Game file !")
        exit(0)

    gd.read_file(game_file)

    web_server = webservice.service_thread(port)
    web_server.httpd.files_dir = files_dir
    web_server.httpd.game_data = gd
    web_server.start()

