#!/bin/bash


../halite -d "60 60" "python3 ../bots/team_a/bot.py" "python3 ../bots/team_b/bot.py" "python3 ../bots/team_c/bot.py" "python3 ../bots/team_d/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/bot.py" "python3 ../bots/team_b/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/bot.py" "python3 ../bots/team_c/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_a/bot.py" "python3 ../bots/team_d/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_b/bot.py" "python3 ../bots/team_c/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_b/bot.py" "python3 ../bots/team_d/bot.py" -q
../halite -d "30 30" "python3 ../bots/team_c/bot.py" "python3 ../bots/team_d/bot.py" -q

