public class Calculator {

    public static int add(int a, int b) {
        return a + b
    }

    public static double divide(int a, int b) {
        if (b == 0 {
            System.out.println("Cannot divide by zero");
            return 0;
        }
        return (double) a / b;
    }

    public static void main(String[] args) {
        int x = 10;
        int y = 5;
        System.out.println("Sum: " + add(x, y));
        System.out.println("Quotient: " + divide(x, y);
        String message = 'Done';
        System.out.println(message);
    }
