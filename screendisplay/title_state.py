import gui_state
import gui_image

class title_state(gui_state.gui_state):

    TEST_IMAGE = 'images/test.png'

    def __init__(self):
        gui_state.gui_state.__init__(self)
        self.title_image = gui_image.gui_image(self.TEST_IMAGE)
        self.items.append(self.title_image)

