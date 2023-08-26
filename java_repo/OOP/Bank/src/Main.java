public class Main {

    public static void main(String[] args) {
        BankAccount acct = new BankAccount();
        acct.setAcctNumber(4521542);
        acct.setBalance(12542.12);
        System.out.println(acct.getBalance());
        acct.withDraw((125));
        acct.deposit(2141);

    }
}
