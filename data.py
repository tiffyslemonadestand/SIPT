base_opp = ['None', 'Brandenburg-Prussia', 'England', 'Sweden']
bc_opp = ['France']
je_opp = ['Russia', "Habsburg"]
pp2_opp = ['Scotland']

base_spirits = ['Lightnings Swift Strike','River Surges in Sunlight', 'Vital Strength of the Earth', 'Shadows Flicker Like Flame', 'Thunderspeaker', 'A Spread of Rampant Green', 'Oceans Hungry Grasp', 'Bringer of Dreams and Nightmares']
bc_spirits = ['Sharp Fangs Behind the Leaves', 'Keeper of the Forbidden Wilds']
je_spirits = ['Stones Unyielding Defiance', 'Shifting Memory of Ages', 'Grinning Trickster Stirs up Trouble', 'Lure of the Deep Wilderness', 'Many minds Move as One', 'Volcano Looming High', 'Shroud of Silent Mist', 'Vengeance as a Burning Plague', 'Starlight Seeks Its Form', 'Fractured Days Split the Sky']
pp1_spirits = ['Heart of Wildfire', 'Serpent Slumbering Beneath the Island']
pp2_spirits = ['Downpour Drenches the World', 'Finder of Paths Unseen']

spirit_aspects = {  'Lightnings Swift Strike': ['pp2:Immense', 'je:Pandemonium', 'je:Wind'],
                    'River Surges in Sunlight': ['je:Sunshine', 'pp2:Travel'],
                    'Vital Strength of the Earth': ['pp2:Might', 'je:Resilience'],
                    'Shadows Flicker Like Flame': ['pp2:Amorphous', 'pp2:Foreboding', 'je:Madness', 'je:Reach'],
                    'Thunderspeaker': [],
                    'A Spread of Rampant Green': [],
                    'Oceans Hungry Grasp': [],
                    'Bringer of Dreams and Nightmares': [],
                    'Sharp Fangs Behind the Leaves': [],
                    'Keeper of the Forbidden Wilds': [],
                    'Stones Unyielding Defiance': [],
                    'Shifting Memory of Ages': [],
                    'Grinning Trickster Stirs up Trouble': [],
                    'Lure of the Deep Wilderness': [],
                    'Many minds Move as One': [],
                    'Volcano Looming High': [],
                    'Shroud of Silent Mist': [],
                    'Vengeance as a Burning Plague': [],
                    'Starlight Seeks Its Form': [],
                    'Fractured Days Split the Sky': [],
                    'Heart of Wildfire': [],
                    'Serpent Slumbering Beneath the Island': [],
                    'Downpour Drenches the World': [],
                    'Finder of Paths Unseen': [],
                    'None': []}

spirit_setup = {    'Lightnings Swift Strike': 'Put 2 presence on your starting board in the highest-numbered Sands.\n',
                    'River Surges in Sunlight': 'Put 1 presence on your starting board in the highest-numbered Wetlands.\n',
                    'Vital Strength of the Earth': 'Put 3 presence on your starting board: 2 in the highest-numbered Mountain, 1 in the highest-numbered Jungle.\n',
                    'Shadows Flicker Like Flame': 'Put 3 presence on your starting board: 2 in the highest numbered Jungle, and one in land #5.\n',
                    'Thunderspeaker': 'Put 2 presence on your starting board: 1 in each of the 2 lands with the most Dahan.\n',
                    'A Spread of Rampant Green': 'Put 2 presence on your starting board: 1 in the highest-numbered Wetland, and 1 in the Jungle without any Dahan. (If there is more than one such jungle, you may choose)\n',
                    'Oceans Hungry Grasp': 'Put 2 presence onto your starting board: 1 in the Ocean, and 1 in a coastal land of your choice.\n',
                    'Bringer of Dreams and Nightmares': 'Put 2 presence on your starting board in the highest-numbered Sands.\n',
                    'Sharp Fangs Behind the Leaves': 'Put 1 presence and 1 beast token on your starting board in the highest-numbered Jungle. Put 1 presence in a land of your choice with a beast token anywhere on the island.\n',
                    'Keeper of the Forbidden Wilds': 'Put 1 presence and 1 wilds token on your starting board in the highest-numbered Jungle.',
                    'Stones Unyielding Defiance': 'Put 2 presence on your starting board: 1 in the lowest-numbered Mountain without Dahan; 1 in an adjacent land that has blight. (if possible) or Sands (if not)\n',
                    'Shifting Memory of Ages': 'Put 2 presence on your starting board in the highest-numbered land that is Sands or Mountain. Prepare 1 moon, 1 Air, and 1 Earth marker (put them by your Special Rules)\n',
                    'Grinning Trickster Stirs up Trouble': 'Put 2 presence on your starting board: 1 in the highest-numbered land with Dahan, and 1 in land #4.\n',
                    'Lure of the Deep Wilderness': 'Put 3 presence on your starting board: 2 in land #8, and 1 in land #7. Add 1 beast token to land #8.\n',
                    'Many minds Move as One': 'Put 1 presence and 1 beast token on your starting board, in a land with a beast token. Note that you have 5 unique power cards.\n',
                    'Volcano Looming High': 'Put 1 presence on your starting board in a mountain of your choice. Push all Dahan from that land.\n',
                    'Shroud of Silent Mist': 'Put 2 presence on your starting board: 1 in the highest-numbered Wetland and 1 in the highest-numbered Mountain.\n',
                    'Vengeance as a Burning Plague': '1 of your presence starts the game already Destroyed. Put 2 presence on your starting board, 1 in a land with blight, 1 in a Wetland without Dahan.\n',
                    'Starlight Seeks Its Form': 'Put 1 presence on your starting board, in a land with blight.\n',
                    'Fractured Days Split the Sky': 'Put 3 presence on your starting board: 1 in the lowest-numbered land with 1 Dahan, and 2 in the highest-numbered land without Dahan. Deal 4 Minor and Major Powers face-up as your initial Days that Never Were cards; in a 1 or 2 player game, instead deal 6 of each. In a 1-board game, gain 1 Time.\n',
                    'Heart of Wildfire': 'Put 3 presence and 2 blight on your starting board in the highest-numbered Sands. (Blight comes from the box, not the blight card)\n',
                    'Serpent Slumbering Beneath the Island': 'Put one presence on your starting board in land #5.\n',
                    'Downpour Drenches the World': 'Put 1 presence on your starting baord in the lowest-numbered Wetlands.\n',
                    'Finder of Paths Unseen': 'Put 1 presence on your starting board in land #d. Put 1 presence on any board in land #1. Not that you have 6 unique power cards.\n',
                    'None': ''}                    

spirit_growth_count = { 'Lightnings Swift Strike': 1,
                        'River Surges in Sunlight': 1,
                        'Vital Strength of the Earth': 1,
                        'Shadows Flicker Like Flame': 1,
                        'Thunderspeaker': 1,
                        'A Spread of Rampant Green': 1,
                        'Oceans Hungry Grasp': 1,
                        'Bringer of Dreams and Nightmares': 1,
                        'Sharp Fangs Behind the Leaves': 2,
                        'Keeper of the Forbidden Wilds': 2,
                        'Stones Unyielding Defiance': 1,
                        'Shifting Memory of Ages': 1,
                        'Grinning Trickster Stirs up Trouble': 2,
                        'Lure of the Deep Wilderness': 2,
                        'Many minds Move as One': 1,
                        'Volcano Looming High': 1,
                        'Shroud of Silent Mist': 1,
                        'Vengeance as a Burning Plague': 1,
                        'Starlight Seeks Its Form': 3,
                        'Fractured Days Split the Sky': 1,
                        'Heart of Wildfire': 1,
                        'Serpent Slumbering Beneath the Island': 2,
                        'Downpour Drenches the World': 1,
                        'Finder of Paths Unseen': 1,
                        'None': 1}

base_scenarios = ['Blitz', 'Guard the Isles Heart', 'None', 'Rituals of Terror', 'Dahan Insurrection']
bc_scenarios = ['Second Wave', 'Powers Long Forgotten', 'Ward the Shores', 'Rituals of the Destroying Flame']
je_scenarios = ['Elemental Invocation', 'Despicable Theft', 'The Great River']
pp1_scenarios = []
pp2_scenarios = ['A Diversity of Spirits', 'Varied Terrains']


#Fear Card counts, taken from Opponent cards
#Dictionary accessed with fear_cards[opponent][app.level]
fear_cards = {'None':                ['9(3/3/3)',
                                      '9(3/3/3)',
                                      '9(3/3/3)',
                                      '9(3/3/3)',
                                      '9(3/3/3)',
                                      '9(3/3/3)'],
              'Brandenburg-Prussia': ['9(3/3/3)', 
                                      '9(3/3/3)',
                                      '10(3/4/3)',
                                      '11(4/4/3)',
                                      '11(4/4/3)',
                                      '12(4/4/4)'],
              'England':            ['10(3/4/3)',
                                      '11(4/4/3)',
                                      '13(4/5/4)',
                                      '14(3/4/5)',
                                      '14(4/5/5)',
                                      '13(4/5/4)'],
              'France':              ['9(3/3/3)',
                                      '10(3/4/3)',
                                      '11(4/4/3)',
                                      '12(4/4/4)',
                                      '13(4/5/4)',
                                      '14(4/5/5)'],
              'Sweden':              ['9(3/3/3)',
                                      '10(3/4/3)',
                                      '10(3/4/3)',
                                      '11(3/4/4)',
                                      '12(4/4/4)',
                                      '13(4/4/5)'],
              'Scotland':            ['10(3/4/3)',
                                      '11(4/4/3)',
                                      '13(4/5/4)',
                                      '14(5/5/4)',
                                      '15(5/6/4)',
                                      '16(6/6/4)'],
               'Russia':              ['10(3/3/4)',
                                       '11(4/3/4)',
                                       '11(4/4/3)',
                                       '12(4/4/4)',
                                       '13(4/5/4)',
                                       '13(4/5/4)'],
               'Habsburg':            ['10(3/4/3)',
                                       '11(4/5/2)',
                                       '12(4/5/3)',
                                       '13(4/5/3)',
                                       '13(4/6/3)',
                                       '14(5/6/3)']                                     
              }

#Dictionary of changes made during game setup based on opponent
#Accessed with setup_changes[opponent][app.level]
setup_changes = { 'None':                ['',
                                          '',
                                          '',
                                          '',
                                          '',
                                          ''],
                  'Brandenburg-Prussia': ['Add one town land #3 on each board\n',
                                          'Put one stage 3 card between Stage I and Stage II\n',
                                          'Remove an additional Stage I card.\n',
                                          'Remove an additional Stage II card.\n',
                                          'Remove an additional Stage I Card.\n',
                                          'Remove all Stage I Cards.\n'],
                  'England':             ['',
                                          'On each board add one city to land #1 and one town to land #2\n',
                                          'Put the High Immigration tile on the invader board to the left of ravage\n',
                                          '',
                                          '',
                                          'Add an additional fear to the pool per player\n'],
                  'France':              ['Return all but 7 towns per player to the box before setup.\n',
                                          'Put the Slave Rebellion Event under the top 3 cards of the event deck.\n',
                                          'On each board add one town to the highest numbered land without a town.\nAdd one town to land 1.\n',
                                          '',
                                          '',
                                          ''],
                  'Sweden':              ['',
                                          'On each board add one city to land #4.\nOn boards where land #4 starts with blight, put that blight in land #5 instead.\n',
                                          '',
                                          'After adding all invaders, discard the top card of the invader deck. On each board add one town to the land of that terrain with the fewest invaders.\n',
                                          '',
                                          'On each board add one town and one blight to land #8.\n(Take the blight from the box, not the blight card)\n'],
                  'Scotland':            ['',
                                          'Add one city to land #2.\nPlace "Coastal Lands" as the 3rd stage II invader card, and move the two stage II cards above it up by one.\n',
                                          '',
                                          'Replace the bottom stage I Card with the bottom stage III card\n',
                                          '',
                                          ''],
                  'Russia':               ['On each board, add one beast and one explorer to the highest-numbered land without towns/cities.\n',
                                           '',
                                           '',
                                           '',
                                           'Put an unused Stage II Invader card under the top 3 fear cards, and an unused Stage III Card under the top 7 fear cards. When revealed, immediately place it in the build space (face up)\n',
                                           ''],
                  'Habsburg':             ['',
                                           'On each board, add one town to land #2 and one town to the highest-numbered land without setup symbols.\n',
                                           '',
                                           '',
                                           'Put the Habsburg Reminder Card under the top 5 invader cards.\n',
                                           '']                                        
                  }

#Global variable for game setup changes based on expansion
#Simple dictionary, access via expansion_setup[expansion] = value
expansion_setup = { 'None': '',
                    'Branch and Claw': 'On each board:\nPut one Beast Token in the lowest land with no printed icons.\nPut one Disease Token in land #2',
                    'Jagged Earth': 'On each board:\nPut one Beast Token in the lowest land with no printed icons.\nPut one Disease Token in land #2',
                    'BC and JE': ''
                    }

#Global variable for invader deck
#dictionary accessed via invader_deck[opponent][level]
invader_deck = { 'None':                ['111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333'],
                 'Brandenburg-Prussia': ['111-2222-33333',
                                         '111-3-2222-3333',
                                         '11-3-2222-3333',
                                         '11-3-222-3333',
                                         '1-3-222-3333',
                                         '3-222-3333'],
                  'England':            ['111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333'],
                  'France':             ['111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333'],
                  'Sweden':             ['111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333'],
                  'Scotland':           ['111-2222-33333',
                                         '11-22-1-C2-33333 (C2 is Coastal Lands Stage II Card)',
                                         '11-22-1-C2-33333 (C2 is Coastal Lands Stage II Card)',
                                         '11-22-3-C2-3333 (C2 is Coastal Lands Stage II Card)',
                                         '11-22-3-C2-3333 (C2 is Coastal Lands Stage II Card)',
                                         '11-22-3-C2-3333 (C2 is Coastal Lands Stage II Card)'],
                  'Russia':             ['111-2222-33333',
                                         '111-2222-33333',
                                         '111-2222-33333',
                                         '111-2-3-2-3-2-3-2-33',
                                         '111-2-3-2-3-2-3-2-33',
                                         '111-2-3-2-3-2-3-2-33'],
                  'Habsburg':           ['111-2222-33333',
                                         '111-2222-33333',
                                         '11-2222-33333',
                                         '11-2222-33333',
                                         '11-2222-33333',
                                         '11-2222-33333']                          
                }

#global variable for the stage 2 invader card flag impact
#dictionary accessed via stage2_flag[opponent] = value
#scotland must be updated during MainApp build due to change to player count
stage2_flag = { 'None': '',
                'Brandenburg-Prussia': 'If the invader card has a flag:\nOn each board with towns or cities: Add one town to a land without a town.\n',
                'England': 'If the invader card has a flag:\nOn each board with towns or cities: Build in the land with the most towns/cities.\n',
                'France': 'If the invader card has a flag:\nAfter exploring, on each board, pick a land of the shown terrain. If it has towns/cities, add one blight. Otherwise add one town.',
                'Sweden': 'If the invader card has a flag:\nAfter invaders explore into each land this phase, if that land has at least as many invaders as dahan, replace one dahan with one town.\n',
                'Scotland': 'If the invader card has a flag:\nOn the single board with the most coastal towns/cities add one town to the (number of players) lands with the fewest towns.\n',
                'Russia': 'If the invader card has a flag: On each board:\nAdd 2 explorers (total) among lands with beasts. If you can\'t, instead add 2 explorers among lands with beasts on a different board.\n',
                'Habsburg': 'If the invader card has a flag:\nAfter exploring: On each board with 4 or fewer blight, add one town to a land without towns/blight. On each board with 2 or fewer blight, do so again.\n'
                }

#allscreen rules has 7 entries instead of the usual 6.  The first entry is for any additional loss condition.
allscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            'Loss condition: If 7 or more towns/cities are ever in a single land, the invaders win.\n',
                            '',
                            '',
                            '',
                            '',
                            'Towns and Cities have +1 health\n',
                            ''],
    'France': [
                            'Loss condition: Invaders win if you ever cannot place a town.\n',
                            '',
                            '',
                            '',
                            '',
                            'When you remove blight from the board, put it on the adversary card instead of on the blight card. As soon as you have 3 blight per player on the card, move it all back to the blight card.\n',
                            ''],
    'Sweden': [             
                            '',
                            '',
                            '',
                            'Towns deal 3 damage. Cities deal 5 damage.\n',
                            '',
                            '',
                            ''],
    'Scotland': [            
                            'Loss condition: If the number of coastal lands with cities is ever greater than (2x # of boards) the invaders win.\n',
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            'Loss condition: Put beasts destroyed by adversary rules on the adversary panel. If there are ever more beasts on that panel than the island, the invaders win.\n',
                            'Explorers do +1 damage.\n',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            'Loss condition: Track how many blight come off the blight cards during ravages that do 8+ damage to the land. If that number ever exceeds players, the invaders win.\n',
                            '',
                            '',
                            '',
                            'Towns in lands without blight are Durable: they have +2 health, and \'Destroy town\' effects instead deal 2 damage (to towns only) per town they could destroy. (\"Destroy all towns\" works normally.)\n',
                            '',
                            '']
    }

# These are the opponent health/damage values
# order is:
# explorer health, town health, city health, explorer damage, town damage, city damage    
opponentmod_rules = {
    'None':                 [
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123'],
    'Brandenburg-Prussia':  [
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123'],
    'England': [             
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '134123',
                            '134123'],
    'France': [
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123'],
    'Sweden': [             
                            '123123',
                            '123123',
                            '123123',
                            '123135',
                            '123135',
                            '123135',
                            '123135'],
    'Scotland': [            
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123'],
    'Russia': [              
                            '123223',
                            '123223',
                            '123223',
                            '123223',
                            '123223',
                            '123223',
                            '123223'],
    'Habsburg': [            
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123',
                            '123123']
    }
    
firstexplorescreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

growthscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

energyscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

powercardscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

fastpowerscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }
    
blightedislandscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }
    
eventscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }
    
fearscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            'If no fear cards are resolved, perform the build from High Immigration Twice on this round.\n'],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            'Fear card effects never remove explorers. If one would, you may instead push that explorer.\n'],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            'When the stage III card is revealed, immediately place it in the build space (face up).\n',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }
    
highimmigrationscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            'If no fear cards were resolved, perform this build Twice.\n'],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

ravagescreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            'If the invaders do at least 6 damage to the land during Ravage, add and extra blight. OThe additional blight does not destroy presence or cascade.\n',
                            '',
                            '',
                            '',
                            'When ravaging adds at least one blight to a land, also add one town to an adjacent land without towns/cities. Cascading blight does not cause this effect.\n',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            'After a ravage card adds blight to a coastal land, add one blight to that board\'s ocean (without cascading). Treat the ocean as a coastal wetland for this rule and for blight removal/movement.\n',
                            'After the ravage step, add one town to each inland land that matches a ravage card and is within one distance of a town/city.\n'],
    'Russia': [              
                            'When ravage adds blight to a land (including cascades), destroy one beast in that land.\n',
                            '',
                            'Ravage cards also match lands with 3 or more explorers. (If the land already matched the ravage card, it still ravages just once.)\n',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            'Ravages do +2 damage (total) if any adjacent lands have towns. (This does not cause lands without invaders to ravage)\n']
    }

buildscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            'Invader build actions affect lands without invaders, if they are adjacent to at least 2 towns/cities before the build action\n',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            'After invaders build in a land with 2 explorers or more, replace all but one explorer there with an equal number of towns.\n',
                            '',
                            'Whenever invaders build a coastal city, add one town to the adjacent land with the fewest towns.\n',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            'In coastal lands, build cards affect lands without invaders, so long as there is an adjacent city.\n',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            'After the normal build step: In each land matching a build card, gather one town from a land not matching a build card. (In board/land order.)\n',
                            'When invaders would build one city in an inland land, they instead build two towns.\n',
                            '',
                            '',
                            '',
                            '']
    }

explorescreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            'After invaders successfully explore into a land which had no towns/cities, add one explorer there.\n',
                            '',
                            '',
                            '',
                            '',
                            'After the normal explore, on each board add one explorer to a land without any.\n'],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            'In coastal lands, explore cards add one town instead of explorer. \'Coastal lands\' invader cards do this for a maximum 2 lands per board.\n',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            'When the Habsburg reminder card is revealed, on each board, add one city to a coastal land without cities and one town to the 3 inland lands with the fewest blight.\n',
                            '']
    }

advancecardsscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            'Remove the High Immigration tile when a stage II card is moved to it.\n',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

slowpowerscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

timepassesscreen_rules = {
    'Brandenburg-Prussia':  [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'England': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'France': [
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Sweden': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Scotland': [             
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Russia': [              
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''],
    'Habsburg': [            
                            '',
                            '',
                            '',
                            '',
                            '',
                            '']
    }

screenTitles = { 'Main': 'Spirit Island Phase Tracker',
                 'SpiritSelect': 'Select Spirits',
                 'BoardSetup': 'Board Setup',
                 'SpiritSetup': 'Spirits Setup',
                 'FirstExplore': 'First Exploration', 
                 'Growth': 'Growth Phase', 
                 'Energy': 'Gain Energy',
                 'PowerCards': 'Select Power Cards', 
                 'FastPower': 'Fast Powers', 
                 'BlightedIsland': 'Blighted Island Effects', 
                 'Event': 'Event Card', 
                 'Fear': 'Fear Cards', 
                 'HighImmigration': 'High Immigration', 
                 'Ravage': 'Invaders Ravage the Island', 
                 'Build': 'Invaders Build on the Island', 
                 'Explore': 'Invaders Explore the Island', 
                 'AdvanceCards': 'Advance the Invader Cards', 
                 'SlowPower': 'Slow Powers', 
                 'TimePasses': 'Time Passes'}

screenDescriptions = {  'FirstExplore': 'Reveal the top card of the Invader deck. The invaders explore that land type. When done exploring, place this card in the Build space.\n', 
                        'Growth': 'Choose one option (unless stated otherwise) next to "Growth" at the upper right of the Spirit panel. Each section is a separate choice. You must do everything shown, but may choose the order.\n', 
                        'Energy': 'Gain an amount of Energy equal to the highest uncovered number on your Energy Presence Track.\n',
                        'PowerCards': 'Select the Power Cards you will use this turn. You must immediately pay Energy for all power cards played, even slow ones. Do not resolve the effects of the Power Cards yet.\n', 
                        'FastPower': 'Resolve fast powers - both Innate Powers on your spirit panel, and power cards played.\n', 
                        'BlightedIsland': '', 
                        'Event': 'Draw and Resolve Event Card', 
                        'Fear': 'If any Fear cards have been earned, pick up the whole face-down stack, flip it over and resolve the cards one at a time in the order they were earned.\n', 
                        'HighImmigration': 'Invaders take this Build action before Ravaging.\n', 
                        'Ravage': 'Look at the Invader Card in the Ravage Action space on the invader board (if any): the Invaders Ravage in each land of the shown type. First, Invaders deal Damage to the land and Dahan. Then, any surviving Dahan fight back.\n', 
                        'Build': 'Look at the Invader Card in the Build Action Space on the Invader board: the Invadrs build in each land of the shown type only.\n', 
                        'Explore': 'Turn the top card of the Invader Deck face-up. Invaders explore in accessible lands of the shown type only, venturing for from Towns and Cities or approaching from the Ocean.\n', 
                        'AdvanceCards': 'Slide all of the Invader cards left.', 
                        'SlowPower': 'Players resolve slow powers, which may be either Innate Powers printed on their Spirit Panel or Power cards they played.\n', 
                        'TimePasses': 'Players discard all Power cards played this turn into their personal discard piles. All elements go away. All Damage done during the turn goes away. If using any reminder tokens for single-turn effects, remove those at this time.\n'}