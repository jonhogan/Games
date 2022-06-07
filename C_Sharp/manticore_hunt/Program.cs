/*

 
                                     /$$   /$$                       /$$                                                                           
                                    | $$  | $$                      | $$                                                                           
                                    | $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$                                                                         
                                    | $$$$$$$$| $$  | $$| $$__  $$|_  $$_/                                                                         
                                    | $$__  $$| $$  | $$| $$  \ $$  | $$                                                                           
                                    | $$  | $$| $$  | $$| $$  | $$  | $$ /$$                                                                       
                                    | $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/                                                                       
                                    |__/  |__/ \______/ |__/  |__/   \___/                                                                         
                                                                                                                
                                                                                                                
                                                                                                                
                                            /$$$$$$$$ /$$                                                       
                                           |__  $$__/| $$                                                       
                                              | $$   | $$$$$$$   /$$$$$$                                        
                                              | $$   | $$__  $$ /$$__  $$                                       
                                              | $$   | $$  \ $$| $$$$$$$$                                       
                                              | $$   | $$  | $$| $$_____/                                       
                                              | $$   | $$  | $$|  $$$$$$$                                       
                                              |__/   |__/  |__/ \_______/                                       
                                                                                                                
                                                                                                                
                                                                                                                
                     /$$      /$$                       /$$     /$$                                        
                    | $$$    /$$$                      | $$    |__/                                        
                    | $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$$$$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
                    | $$ $$/$$ $$ |____  $$| $$__  $$|_  $$_/  | $$ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$
                    | $$  $$$| $$  /$$$$$$$| $$  \ $$  | $$    | $$| $$      | $$  \ $$| $$  \__/| $$$$$$$$
                    | $$\  $ | $$ /$$__  $$| $$  | $$  | $$ /$$| $$| $$      | $$  | $$| $$      | $$_____/
                    | $$ \/  | $$|  $$$$$$$| $$  | $$  |  $$$$/| $$|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$
                    |__/     |__/ \_______/|__/  |__/   \___/  |__/ \_______/ \______/ |__/       \_______/
                                                                                                                
                                                                                                                
                                                                                                                
    Player 1: Enters a range for the Manticore Airship
    Player 2: Tries to guess the distance

    City Health = 15
    Manticore Health = 10

    The Manticore will damage the city for 1 point each round it survives.

    Most rounds the player will deal 1 point of damage per hit on the Manticore. If the rounds level is a multiple of 3 (level % 3 = 0), the play will deal 3
    points of lightning damage. If the rounds level is a multiple of 5 (level % 5 = 0), the play will deal 5 points of fire damage. However, if the level is a
    multiple of both 3 and 5, the player will deal a total of 8 points of fire and lightning damage.
*/

int mHealth;                // Manticore health
int cHealth;                // City health
int level;                  // Level/round the game it on.
bool gameLoop = true;       
bool pOneTurn = true;       // Tracks if player one has made their turn
int distance;               // Distance of the Manticore
int pTwoGuess;              // Guess from Player two

while (gameLoop){

    while (pOneTurn){
        mHealth = 10;
        cHealth = 15;
    }

}