package stronghold;

/**
 * Created by spencedalley on 9/17/16.
 */
public class Rabbits {

    public Rabbits() {
        super();
    }

    public int rabbitRelation(int n, int k) {
        int a = 1;
        int b = 1;

        for (int i = 2; i < n; i++) {
            a = b;
            b = k * a + b;
        }

        return b;
    }
}
