Box State = Box.Open;
string newState = " ";
Console.WriteLine("Before you is an open box.");
Console.WriteLine("You can change the state of the box by closing it when open, open or lock it when closed, unlocking it when locked.");

while(true){
    Console.WriteLine("What would you like to do to the box? (Open, Close, lock, or Unlock)");
    newState = Console.ReadLine();

    if(State == Box.Open && (newState == "Close" || newState == "close")){
        Console.WriteLine("You closed the box.");
        State = Box.Closed;
    }else if(State == Box.Closed && (newState == "Open" || newState == "open")){
        Console.WriteLine("You open the box");
        State = Box.Open;
    }else if(State == Box.Closed && (newState == "Lock" || newState == "lock")){
        Console.WriteLine("You lock the box.");
        State = Box.Locked;
    }else if(State == Box.Locked && (newState == "Unlock" || newState == "unlock")){
        Console.WriteLine("You unlock the box.");
        State = Box.Closed;
    }else{
        Console.WriteLine("You can't do that. If the box is open, you can close it. If it is closed, you can open or lock it. If it is locked, you can unlock it.");
    }
}

enum Box{
    Open,
    Closed,
    Locked
}