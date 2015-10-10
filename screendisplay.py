import screendisplay

if __name__ == '__main__':
    viewport = screendisplay.viewport(800, 600)

    client = screendisplay.http_client('localhost', 8080)
    title = screendisplay.title_state()

    print client.get_teams()
    print client.get_game_state()
    print client.get_categories()
    print client.get_points_table()
    print client.get_categories_ranks()

    viewport.push(title)
    #viewport.run()
