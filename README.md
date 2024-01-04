# IDS FINAL PROJ _ STEAM GAME RATINGS
The final project of Introduction to Data Science
![alt text](https://github.com/cheesepp/steam_game_ratings/blob/main/deploy/static/cover.jpg)
## Table of Contents

 - [Information](#information)
 - [Introduction](#introduction)
 - [Project Structure](#project-structure)
 - [Project Plan](#project-plan)
 - [Usage](#usage)

## Information

| Student ID | Name                   |
|------------|------------------------|
| 21120576   | Trần Đình Nhật Trí     |
| 21120501   | Nguyễn Ngọc Gia Minh   |
| 21120590   | Nguyễn Thủy Uyên       |

## Introduction

- This is the Final Project of class **Introduction to Data Science - 21_21** (2023).
- This project's main objective is to analyze and predict game ratings on the Steam website. Our team will conduct an in-depth exploration of the Steam system to identify relevant data and gain insights into patterns that can help us predict whether a game will be successful or not. Our ultimate goal is to find the best solution to estimate a game's success before it is released to the public.

## Project Structure

```
📦steam_game_ratings
├──📦data                          # constains all data for the project
│   ├──📜steam_game.csv            # raw data
│   └──📜processed.csv             # cleaned data
├──📦notebooks                     # contains all jupyter notebooks of the project
│   ├──📜crawl.ipynb               # used to retrieve data from url
│   ├──📜preprocessing.ipynb       # analyzing and adjustment the data
│   ├──📜eda_questions.ipynb       # exploratory and questions about data
│   ├──📜data_modeling.ipynb       # training a ML model for data
    ├──📜model.pkl                 # model of the project
    └──📜fined_tune.pkl            # fined-tune model
├──📦deploy                        # contains the source code for deployment
│   ├──📜view.py                   # main source code for deployment
│   ├──📦statics                   # contains static files (image)
│   │   └──📜cover.png
│   └──📦templates                 # contains UI of product
│       ├──📜after.html
│       └──📜home.html
└──📜README.md
```

## Project Plan

[Trello - Project management](https://trello.com/b/jXnkAonb/steam-game-ratings)

## Usage

1. Clone repository to your device

```
  git clone https://github.com/cheesepp/steam_game_ratings.git
```
2. Open Jupyter Notebook (Anaconda/Miniconda/...)

3. Run the .inpynb files in notebooks folder (optional if you just want to use the deployed model)

- How to deploy project's model:
Open the shell or terminal
```
pip install Flask
cd deploy
python view.py
Wait to get the url and run the server...
```
