import java.lang.reflect.Method;

public class TestCase implements Test{
    public final String name;
    public TestCase(String name) { this.name = name; }
    public void setUp(){}
    public void tearDown(){}

    public void run(TestResult result) {
        result.testStarted();
        setUp();

        try {
            Method method = getClass().getMethod(name);
            method.invoke(this);
        } catch (Exception e) {
            result.testFailed();
        }

        tearDown();
    }
}
