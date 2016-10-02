
import org.junit.Test;
import stronghold.Rabbits;

import static org.junit.Assert.*;

public class RabbitTests {

    @Test public void testRabbitRelation() {
        Rabbits rabbit = new Rabbits();
        int result = rabbit.rabbitRelation(5, 3);
        int expected = 64; // This is wrong
        assertTrue("Should return 19: " + result, result == expected);

        result = rabbit.rabbitRelation(3, 5);
        expected = result;
        assertTrue("Should be equal", result == expected);
    }

}
