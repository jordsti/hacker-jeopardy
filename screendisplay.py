import screendisplay

if __name__ == '__main__':
    viewport = screendisplay.viewport(800, 600)

    title = screendisplay.title_state()
    viewport.push(title)
    viewport.run()
