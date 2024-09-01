import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int number = random.nextInt(100) + 1;
        int guess = 0;

        System.out.println("Guess a number between 1 and 100:");

        while (guess != number) {
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();

            if (guess < number) {
                System.out.println("Your guess is too low!");
                System.out.println("Please try again!");
            } else if (guess > number) {
                System.out.println("Your guess is too high!");
                System.out.println("Please try again!");
            } else {
                System.out.println("Well done! You've guessed the right number.");
            }
        }

        scanner.close();
    }
}
