monsters = { #Gives certain monsters for story level
    "Beginning": [["Goblin", "Cat Noir", "Chomper"],[5, 3, 2]],
    "A New Leaf" : [["Hoboglin", "Buck I","LeGoat","Kitten Net"],[3, 2, 2,2]],
    "The Might of the Novice" : [["Brick Master", "EGGxcelent", "Like a Boss"],[2,2,1]],
}
monstersClear = {
    #Empty board to store each monsters position
    #need to make it so when new level it also gets cleared: Not difficult
    #need to make it so armor wearing reduces damage
}
#Maybe change system so monsters give experience that can boost leveling up
#Maybe add clases like mage where you can boost your magica or fighting skills
#Make a skill tree
storyBoardMon = {#monsters needed to kill and how many of each monster needed to kill to advance level as long as collected items
    "Beginning" : [["Goblin", "Cat Noir", "Chomper"],[3, 1, 1]],
    "A New Leaf" : [["Hoboglin", "Buck I","LeGoat"],[2, 1, 1]],
    "The Might of the Novice" : [["Brick Master", "EGGxcelent", "Like a Boss"],[2, 1, 1]],
}
monMDandHP = { #Gives [Max damage, health, ["Award"], max drop count, Should add new one for probability of drop] Maybe add buffs like posion damage and stuff Add Award
    #Make it so you have slash between tiems so they can drop more than one
    #(TO DO) Have to make another array that gives each drop its own max drop count - similar to what i did with scattering items
    #[Max DG, Health ['item' rewards],[[min num, highest num for item drop chace]], If I want drop automatic no matter what like a boss add this int of 1 to make it automatic]
    "Goblin" : [5, 10, ["Rock", "Iron Ore", "Stick"], [[0,3], [0,3], [0,4]], 0], #make second to last number max amount each item can drop can make it a list
    "Cat Noir" : [8, 20, ["Stone Axe", "Stone", "Iron Ingot"], [[0,1], [1,4], [1,3]], 0], #or make it so each item has that specific probabilty to drop and rerolls for each item
    "Chomper" : [12, 30, ["Pine Arrow", "Iron Ingot", "Iron Axe"], [[0,5], [2,6], [0,1]], 0],
    
    "Hoboglin" : [12, 40, ["Iron Armor", "Iron Ingot"], [[0,1], [3,5]], 0],
    "Buck I" : [15, 50, ["Gun Powder", "Flipers", "Apple"], [[0,5], [1,1], [0,3]], 0],
    "LeGoat" : [20, 60, ["Flint", "Iron Ingot"], [[0,6], [2,9]], 0],

    "Brick Master" : [20, 60, ["Iron Armor", "Iron Ore", "Flint"], [[1,1], [3,6], [1,5]], 0],
    "EGGxcelent" : [25, 70, ["Pine Sap", "Raw Egg", "Iron Ore", "Gun Powder"], [[0,3], [1,4], [0,4], [1,4]], 0],
    "Like a Boss" : [30, 80, ["Aragon's Blade", "Bomb"], [[1,1], [4,7]], 0],

    "Kitten Net" : [10, 100, ["Diamond","Iron Ingot","Boss Key"], [[1, 4],[3,5],[1,1]], 0], #Empty monster
    #(TO DO) Change it so monsters arent as hard to kill, or if they are make drops better
}
monsterAward = { #Gives awards based on destorying bosses, however 
                    #Fucntion that gives award gives a random amount of it

}
#CREATE A SYSTEM TO PLACE CERTAIN MONSTERS IN A CERTAIN AREA AT ALL TIMES, LIKE BOSS ROOMS ["MONSTER"],[LOCATION]
#so when it loADS IT ALWAYS PLACES MONSTER IN THAT SPOT