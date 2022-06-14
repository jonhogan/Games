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

    Most rounds the player will deal 1 point of damage per hit on the Manticore. If the rounds level is a multiple of 3 (level % 3 = 0), the player will deal 3
    points of lightning damage. If the rounds level is a multiple of 5 (level % 5 = 0), the player will deal 5 points of fire damage. However, if the level is a
    multiple of both 3 and 5, the player will deal a total of 10 points of fire and lightning damage.
*/

int mHealth = 0;                // Manticore health
int cHealth = 0;                // City health
int level = 0;                  // Level/round the game it on.
bool gameLoop = true;       
bool pOneTurn = true;       // Tracks if player one has made their turn
int distance = 0;               // Distance of the Manticore
char replay = 'y';

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
    --cHealth; // The Manticore AirShip deals one point of damage to the city per round
    level++;   // Increase the level each round

    if (mHealth < 1 || cHealth < 1){
        
        if(mHealth < 1){
            Console.WriteLine("You have destroyed the Airship, Manticore!");
            Console.Write("Would you like to play again? (y/n): ");
            replay = Convert.ToChar(Console.ReadLine());

            if (replay == 'y'){
                pOneTurn = true;
            }else{
                gameLoop = false;
            }
        }else if(cHealth < 1){
            Console.WriteLine("The Airship has destroyed you city. Better luck next time.");
            Console.Write("Would you like to play again? (y/n): ");
            replay = Convert.ToChar(Console.ReadLine());

            if (replay == 'y'){
                pOneTurn = true;
            }else{
                gameLoop = false;
            }
        }

    }

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
    Console.Clear();
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
    int pGuess; // Player 2 guess

    Console.Write("What range would you like to fire at? (0-100) ");
    pGuess = Convert.ToInt32(Console.ReadLine());

    while(pGuess < 0 || pGuess > 100){
        Console.Write("Invalid guess, please try again. Enter a guess from 0 to 100:  ");
        pGuess = Convert.ToInt32(Console.ReadLine());
    }

    if(pGuess < dist){
        Console.WriteLine("Your shot fell short!");
    }else if(pGuess > dist){
        Console.WriteLine("You overshot your target!");
    }else{ // If hit, calculate the damage done

        if(lev % 3 == 0 && lev % 5 == 0){
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine("You hit the Manticore for 10 points of Lightning and Fire damage!");
            dmg = 10;
            Console.ForegroundColor = ConsoleColor.White;
        }else if(level % 3 == 0){
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("You hit the Manticore for 3 points of Lightning damage!");
            dmg = 3;
            Console.ForegroundColor = ConsoleColor.White;
        }else if (level % 5 == 0){
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("You hit the Manticore for 5 points of Fire damage!");
            dmg = 5;
            Console.ForegroundColor = ConsoleColor.White;
        }else{
            Console.WriteLine("You hit the Manticore for 1 points of normal damage!");
            dmg = 1;
        }

    }

    Thread.Sleep(500);

    return (mant -= dmg);
}