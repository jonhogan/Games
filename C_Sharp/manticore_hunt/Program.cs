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
    multiple of both 3 and 5, the player will deal a total of 10 points of fire and lightning damage.
*/

int mHealth = 0;                // Manticore health
int cHealth = 0;                // City health
int level = 0;                  // Level/round the game it on.
bool gameLoop = true;       
bool pOneTurn = true;       // Tracks if player one has made their turn
int distance = 0;               // Distance of the Manticore
//int pTwoGuess = 0;              // Guess from Player two

while (gameLoop){

    while (pOneTurn){
        // First round of the game
        // Set Manticore and City health and level
        mHealth = 10;
        cHealth = 15;
        level = 1;

        // Method call to set the distance
        distance = PlayerOne();
        pOneTurn = false;
    }

    hud(mHealth, cHealth, level);
    mHealth = p2Turn(mHealth, level, distance);

}

int PlayerOne(){
    int dist;
    Console.Write("What is the distance do you want to set the Manticore? (Enter a number between 0-100): ");
    dist = Convert.ToInt32(Console.ReadLine());
    Console.Clear();

    // Return the player defined distance
    return dist;
}

void hud(int mHealth, int cHealth, int level){
    // Display the level status
    Console.WriteLine("Status:   Level: " + level + "   City Health: " + cHealth + "/15   Manticore Health: " + mHealth + "/10");

    // Inform the player how much damage can be expected this round
    if(level%3 == 0 && level%5 == 0){
        Console.WriteLine("The cannon is expected to deal 10 point of damage this round.");
    }else if(level%3 == 0){
        Console.WriteLine("The cannon is expected to deal 3 point of damage this round.");
    }else if(level%5 == 0){
        Console.WriteLine("The cannon is expected to deal 5 point of damage this round.");
    }else{
        Console.WriteLine("The cannon is expected to deal 1 point of damage this round.");
    }

}

int p2Turn(int mant, int lev, int dist){
    // Set default damage to 0
    int dmg = 0;



    return (mant -= dmg);
}