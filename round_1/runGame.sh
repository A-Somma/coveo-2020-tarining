#!/bin/bash


../halite -d "60 60" "python3 ../bots/team_a/src/bot.py" "python3 ../bots/team_b/src/bot.py" "python3 ../bots/team_c/src/bot.py" "python3 ../bots/team_d/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/src/bot.py" "python3 ../bots/team_b/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/src/bot.py" "python3 ../bots/team_c/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/src/bot.py" "python3 ../bots/team_d/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_b/src/bot.py" "python3 ../bots/team_c/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_b/src/bot.py" "python3 ../bots/team_d/src/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_c/src/bot.py" "python3 ../bots/team_d/src/bot.py" -q

