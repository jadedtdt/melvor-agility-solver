import csv

max_mastery = True

def load_file():
    with open('data/obstacle_data_large.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        tiers = {}
        for inner_row in reader:
            print(inner_row['Set'], inner_row['XP'], inner_row['Time (s)'])
            tier = str(inner_row['Set'])
            print("tier", tier)
            if tiers.get(tier, None) == None:
                tiers[tier] = []
            tiers[tier].append(inner_row)

        max_obstacle_comb = ''
        max_xp_per_s = 0
        total = 3*3*5*5*5*5*5*5*5*5
        progress = 0
        for t1 in range(0, len(tiers['1'])):
            for t2 in range(0, len(tiers['2'])):
                for t3 in range(0, len(tiers['3'])):
                    for t4 in range(0, len(tiers['4'])):
                        for t5 in range(0, len(tiers['5'])):
                            for t6 in range(0, len(tiers['6'])):
                                for t7 in range(0, len(tiers['7'])):
                                    for t8 in range(0, len(tiers['8'])):
                                        for t9 in range(0, len(tiers['9'])):
                                            for t10 in range(0, len(tiers['10'])):
                                                total_xp = 0
                                                total_xp_mod = 0.0
                                                total_time = 0
                                                total_time_mod = 0.0
                                                total_obstacles = ''
                                                for i in range(0+1, 10+1):
                                                    tn = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
                                                    total_xp += int(tiers[str(i)][tn[i-1]]['XP'])
                                                    #print("xp", total_xp)
                                                    total_xp_mod += float(tiers[str(i)][tn[i-1]]['Passive Agility Bonus'])
                                                    total_xp_mod += (float(tiers[str(i)][tn[i-1]]['Passive Agility Penalty']) if not max_mastery else float(tiers[str(i)][tn[i-1]]['Passive Agility Penalty'])/2)
                                                    #print("xp_mod", total_xp_mod)
                                                    total_time += (int(tiers[str(i)][tn[i-1]]['Time (s)']) * (1+(0 if not max_mastery else (-9*0.03))))
                                                    #print("time", total_time)
                                                    total_time_mod += float(tiers[str(i)][tn[i-1]]['Agility Interval Modifier'])
                                                    #print("time_mod", total_time_mod)
                                                    total_obstacles += tiers[str(i)][tn[i-1]]['Abbr']
                                                    #print("obstacles", total_obstacles)

                                                total_xp_s = (total_xp*(1+total_xp_mod)) / (total_time*(1+total_time_mod))
                                                #print("xp adj", (total_xp*(1+total_xp_mod)))
                                                #print("time adj", (total_time*(1+total_time_mod)))
                                                #print("xp_per_s", total_xp_s)

                                                # if total_obstacles == '1CN2BB3PJ4GJ5CC':
                                                    # exit()

                                                progress += 1
                                                print('Progress: {}%'.format((progress/total)*100))

                                                if total_xp_s > max_xp_per_s:
                                                    max_xp_per_s = total_xp_s
                                                    max_obstacle_comb = total_obstacles
                                                    print('New best is {} at {} xp/s'.format(max_obstacle_comb, max_xp_per_s))

        print("max xp_per_s is {} with obstacles {}".format(max_xp_per_s, max_obstacle_comb))

def load_file_small():
    with open('data/obstacle_data_small.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        tiers = {}
        for inner_row in reader:
            print(inner_row['Set'], inner_row['XP'], inner_row['Time (s)'], inner_row['XP'])
            tier = str(inner_row['Set'])
            print("tier", tier)
            if tiers.get(tier, None) == None:
                tiers[tier] = []
            tiers[tier].append(inner_row)

        max_obstacle_comb = ''
        max_xp_per_s = 0
        total = 3*3*5*5*5
        progress = 0
        for t1 in range(0, len(tiers['1'])):
            for t2 in range(0, len(tiers['2'])):
                for t3 in range(0, len(tiers['3'])):
                    for t4 in range(0, len(tiers['4'])):
                        for t5 in range(0, len(tiers['5'])):
                            total_xp = 0
                            total_xp_mod = 0.0
                            total_time = 0
                            total_time_mod = 0.0
                            total_obstacles = ''
                            for i in range(0+1, 5+1):
                                tn = [t1, t2, t3, t4, t5]
                                total_xp += int(tiers[str(i)][tn[i-1]]['XP'])
                                print("xp", total_xp)
                                total_xp_mod += float(tiers[str(i)][tn[i-1]]['Passive Agility Bonus'])
                                total_xp_mod += (float(tiers[str(i)][tn[i-1]]['Passive Agility Penalty']) if not max_mastery else float(tiers[str(i)][tn[i-1]]['Passive Agility Penalty'])/2)
                                print("xp_mod", total_xp_mod)
                                total_time += (int(tiers[str(i)][tn[i-1]]['Time (s)']) * (1+(0 if not max_mastery else (-9*0.03))))
                                print("time", total_time)
                                total_time_mod += float(tiers[str(i)][tn[i-1]]['Agility Interval Modifier'])
                                print("time_mod", total_time_mod)
                                total_obstacles += tiers[str(i)][tn[i-1]]['Abbr']
                                print("obstacles", total_obstacles)

                            total_xp_s = (total_xp*(1+total_xp_mod)) / (total_time*(1+total_time_mod))
                            print("xp adj", (total_xp*(1+total_xp_mod)))
                            print("time adj", (total_time*(1+total_time_mod)))
                            print("xp_per_s", total_xp_s)

                            # if total_obstacles == '1CN2BB3PJ4GJ5CC':
                                # exit()

                            progress += 1
                            print('Progress: {}%'.format((progress/total)*100))

                            if total_xp_s > max_xp_per_s:
                                max_xp_per_s = total_xp_s
                                max_obstacle_comb = total_obstacles
                                print('New best is {} at {} xp/s'.format(max_obstacle_comb, max_xp_per_s))

        print("max xp_per_s is {} with obstacles {}".format(max_xp_per_s, max_obstacle_comb))


def main():
    load_file()

main()
