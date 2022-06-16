Box State = Box.Open;
string newState = " ";
Console.WriteLine("Before you is an open box.");
Console.WriteLine("You can change the state of the box by closing it when open, open or lock it when closed, unlocking it when locked.");

while(true){
    Console.WriteLine("What would you like to do to the box? (Open, Close, lock, or Unlock)");
    newState = Console.ReadLine();

    if(State == 0 && (newState == "Close" || newState == "close")){
        Console.WriteLine("You closed the box.");
    }else if(State == 1 && (new))
}

enum Box{
    Open,
    Closed,
    Locked
}