# melvor-agility-solver
Brute force solver to find out the most optimal Agility Obstacles because my brain is too small to actually try to compute it myself.

There is a boolean field, max_mastery that can be toggled on or off, this is for assuming 99 mastery on all obstacles to benefit from the agility interval upgrades and the half penalty bonuses.

There is a small file and a large file, I used the small file for testing the algorithms (mainly involving xp bonuses or penalties as well as interval bonuses). You could adjust the small file to see what is the best at each obstacle tier (i.e. 7) by adding more rows to the csv.

How to run: `python3 main.py`

Output for the large file: `max xp_per_s is 33.26484018264839 with obstacles 1CN2BB3BS4GJ5MC6TB7HT8TH9IJ10BM`
