import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class BankAccount {
    private String lastName;
    private String firstName;
    private String email;
    private int acctNumber;
    private double balance;

    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Z0-9._%+-]+@[A-Z0-9-]+\\.[A-Z]{2,6}$",
            Pattern.CASE_INSENSITIVE);

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setAcctNumber(int acctNumber) {
        this.acctNumber = acctNumber;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setEmail(){
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Enter your email");
            email = scanner.nextLine();
            if(validateEmail(email)){
                break;
            }else{
                System.out.println("Invalid email, try again\n");
            }
        }

        scanner.close();
    }


    private boolean validateEmail(String email){
        Matcher matcher = EMAIL_PATTERN.matcher(email);
        return matcher.matches();
    }


}
