# Typing Game - pygame
* **English**
* [Português](README-ptBR.md)
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Thinato/pygame-typing">
    <img src="assets/img/logo128.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">pygame-typing</h3>

  <p align="center">
    A typing game made with pygame.
    <br />
    <a href="https://github.com/Thinato/pygame-typing/blob/main/game.py"><strong>Main Game file »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Thinato/pygame-typing/blob/main/demo/demo.gif">View Demo</a>
    ·
    <a href="https://github.com/Thinato/pygame-typing/issues">Report Bug</a>
    ·
    <a href="https://github.com/Thinato/pygame-typing/pulls">Request Feature</a>
  </p>
</div>


## About
This is an implementation of a typing game, the objective is to not let the words come to the left side by typing them and pressing return. Each word has a score that when you type it is registred below, this score is also used to make the game harder and harder as you progress through.

This project was heavily inspired by [bisqwit's](https://bisqwit.iki.fi/) typing game ([wspeed](https://bisqwit.iki.fi/wspeed/))

![gif demonstrating the game being played][demo]

## Requirements
* Python 3.10
* pygame 2.1.2

## How to Start the Game
Run main.py<br/>
`$ python main.py`

## Features
* Scoring system
* Difficulty increase over progress
* Leaderboarding system
* Words per minute meter
* Accuracy meter
* Easy to create new words and word_lists

## How to create word_lists
1. Go to 'word_lsts' folder
2. Create a new text (.txt) file
3. Type each word in each line of the file
4. Then save the file
5. Create a new empty text file in 'leaderboards' folder with the same name of your word_list file.

## Assets used
* [jsfxr](https://sfxr.me/) - An 8 bit sound generator made with JavaScript by Eric Fredricksen, the original version (sfxr) was made by DrPetter
* Background music - An 8 bit port of J.S. Bach: [Little Fugue in G minor (BWV 578)](https://www.youtube.com/watch?v=Bbox4oi6HjA), the remix was made by [MajorNebula](https://www.youtube.com/channel/UCyWw_f8wEU3PIEO2LaKgoUw)


## Further Reading
* [pygame](https://www.pygame.org/wiki/about)
* [wspeed](https://bisqwit.iki.fi/wspeed/)
* [jsfxr](https://sfxr.me/)
* [background music](https://www.youtube.com/watch?v=ZAwYwK4Ujas)




<!-- MARKDOWN LINKS & IMAGES -->
[demo]: demo/demo.gif
