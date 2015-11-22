import java.util.*;

class IntegerHash implements Hashable {

    public Integer value;

    public IntegerHash(int value) {
        this.value = new Integer(value);
    }

    @Override
    public int hashValue() {
        return value.hashCode();
    }

    @Override
    public int compareTo(Hashable h) {
        IntegerHash other = (IntegerHash) h;
        return value.compareTo(other.value);
    }

    @Override
    public String toString() {
        return "" + value;
    }

}

public class Test {

    public static void main(String[] args) {
        ChainHashing<IntegerHash> tmp = new ChainHashing<IntegerHash>();
        Random r = new Random(1000);
        for(int i = 0; i < 20; i++) {
            int t = r.nextInt(1000);
            tmp.insert(new IntegerHash(t));
        }
        tmp.display();
    }



}
