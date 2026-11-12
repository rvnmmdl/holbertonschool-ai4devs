import java.util.ArrayList;
import java.util.List;

public class Bug3 {
    public static List<Integer> removeDuplicates(List<Integer> values) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < values.size(); i++) {
            if (!result.contains(values.get(i))) {
                result.add(values.get(i));
            }
            values.remove(i);
        }

        return result;
    }

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>(List.of(1, 2, 2, 3, 3));
        System.out.println(removeDuplicates(values));
    }
}
