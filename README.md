# MOOD-SONG WIZARD 🎵🧙‍♂️  
#### Video Demo: https://youtu.be/Ar28i-HlCp8
#### Description:

We humans experience a wide range of emotions, and it’s important to acknowledge and embrace them. This project, “Mood-Song Wizard,” is a command-line program that functions like a mini therapist — one that speaks the universal language of music. Given a user's mood, it uses the Spotify API to fetch songs related to that mood and recommends one at random. The user is then prompted for feedback, and the response is recorded in a report file for future reference.

This project was written entirely in Python and makes use of the third-party `Spotipy` library to interact with the Spotify API. It leverages either of two authentication flows depending on developer preference: the **Client Credentials Flow** (used in the final submission) or the **Authorization Code Flow** (also explored and tested). The former provides access to Spotify’s public catalog of songs anonymously, while the latter would allow for actual changes to a logged-in user’s account — such as creating playlists and adding tracks in real-time.

---

## Project Structure and Files:

- `project.py`: This is the main program. It begins by prompting the user to describe how they're feeling. The input is validated to ensure it contains no numbers or unsupported characters. The program then uses Spotify’s search endpoint to retrieve the top 50 tracks related to that mood. A single track is chosen randomly, and the program outputs its name, artist, and a clickable URL that leads to the song on Spotify.

  After the recommendation, the program asks the user whether they liked the song. If they respond "Yes", the song is saved to a local file called `Favorites.txt`. If they respond "No", the song is instead saved to `Not Favorites.txt`. These files serve as a session report, allowing the user (or developer) to review their preferences later.

  Optionally, with the Authorization Code Flow enabled, liked songs can also be added to the user’s Spotify account via a new or existing playlist titled "Favorites".

- `test_project.py`: This file contains five automated tests written using the `pytest` framework. These tests validate the structure and behavior of the `recommend_song` and `get_user_mood` functions. Because the recommendation logic involves Python’s `random` module, some tests only check the structure of the output rather than exact content.

- `Favorites.txt` and `Not Favorites.txt`: These are the two simple output files created during user sessions. They log the songs that were liked or disliked by the user, including song title, artist, and a Spotify URL.

- `README.md`: This file — written to fulfill CS50’s documentation standards — provides a comprehensive overview of the project, its functionality, files, design decisions, and usage.

- `requirements.txt`: Lists all Python packages required to run the program (namely `spotipy` and `black` for formatting).

---

## Design Considerations:

I debated between implementing the Authorization Code Flow or sticking with the Client Credentials Flow. While the former would allow the app to directly update the user’s Spotify account — adding liked songs to a real playlist — I ultimately chose the Client Credentials Flow for the final submission. It was simpler to implement, avoided dealing with redirect URIs and tokens, and still allowed me to focus on core functionality. That said, I did explore and successfully implement the Authorization Code Flow in a separate version, which I will include in my GitHub repository for reference (username: dhaveed-0).

Another design decision involved user experience. I used emojis extensively throughout the CLI to simulate a more engaging, GUI-like experience. Feedback prompts, song output, and even error messages are styled in a way that brings personality and polish to an otherwise text-only program.

I also ensured that my code was readable and maintainable. Long lines were broken up and reformatted using the `black` module. I added comments throughout the code to explain each section clearly — both for my own understanding and for anyone else who might read or use this project.

---

## License:

This project is intended for academic use only. Please replace the included 'client_id' and 'client_secret' with your own if testing.

The client id and client secret used in my project were obtained after I created a app in Spotify at 'Spotify for Devlopers' - "https://developer.spotify.com/" (Log in with Spotify account)

In this context, an “app” refers to the platform Spotify provides for hosting and authenticating your program. The client_id and client_secret are like your app’s username and password — used to authenticate your application (not you personally) when accessing Spotify’s Web API via Spotipy.

- client_id      # A unique identifier for your Spotify developer app
- client_secret  # A secret key proving your app is legit (keep it safe!)

---

## Final Thoughts:

This project has been an incredibly fulfilling part of my journey through CS50’s Introduction to Programming with Python. It combined creativity with logic and gave me hands-on experience working with third-party APIs, Python modules, testing frameworks, and documentation best practices. Most importantly, it helped me understand how even a command-line app can provide a fun, personalized, and engaging user experience. I’m proud of the result, and I hope you enjoy running the Mood-Song Wizard as much as I enjoyed building it.


This was my CS50 Final Project!

---
