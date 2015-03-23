# hacker-jeopardy
Jeopardy Game with a Mobile and HTML Front-end for the animator

## Projects breakdown

 - Web Service : This will handle all the game data, so you will call this service to ask a question, attribute points... etc
 
 - Jeopardy Interface : Here, we need to do a simple interface to show on a projector or a big screen for the crowd.
      
      - Show the question board, with question and categories
      
      - Show the current asked question with the team, maybe implement a little timer and play the classic jeopardy song
      
      - Show each teams score
 
 - Mobile (Android apps) 
 
      - Show the current game information by fetching data from the web service
      
      - Can ask a question to a team, and show the answer
      
      - Choose if the answer was valid (and add points) or ask to another team
      
 
 - Web Interface
      
      - Javascript mostly
      
      - I'm using this interface to this the web service at the moment, this will does the same things as the Mobile Apps
      
### To Do

  - Ask to another team (web interface and web service)
  - Ask a question from the web interface (choose category and points value)
  - Add points to a team (by drinking beers mostly)
  - Better game file, game1.txt is only for test purpose at the moment
  - Current Game State saving, in case of a fatal crash
  - Game Interface (PyGame maybe, because GUI Interface with widget will not be revelant)
