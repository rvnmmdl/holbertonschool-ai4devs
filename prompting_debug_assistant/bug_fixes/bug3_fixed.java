class Calculator {

    public static int add(int a, int b) {
        return a + b;
    }

    public static double divide(int a, int b) {
        if (b == 0) {
            System.out.println("Cannot divide by zero");
            return 0;
        }
        return (double) a / b;
    }

    static void check(String label, double expected, double actual) {
        boolean ok = expected == actual;
        System.out.println(label + " | expected=" + expected + " | actual=" + actual + " | " + (ok ? "PASS" : "FAIL"));
        if (!ok) {
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        int x = 10;
        int y = 5;
        System.out.println("Sum: " + add(x, y));
        System.out.println("Quotient: " + divide(x, y));
        String message = "Done";
        System.out.println(message);

        check("add(10, 5)", 15, add(10, 5));
        check("add(-1, 1)", 0, add(-1, 1));
        check("divide(10, 5)", 2.0, divide(10, 5));
        check("divide(7, 2)", 3.5, divide(7, 2));
        check("divide(1, 0)", 0.0, divide(1, 0));
        System.out.println("All tests passed");
    }
}
