import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 여러개의 테스트를 추가해서 한번에 데이터를 가져오는 클래스 
 */
// Test interface를 구현한 것을 진행하는 version
public class TestSuite implements Test {
    List<Test> tests = new ArrayList<>();

    public TestSuite(){}
    public TestSuite(Class<? extends Test> testClass) {
        Arrays.stream(testClass.getDeclaredMethods())
            .filter(m -> m.getName().startsWith("test")) // 이름 앞 글자가 "test"인 경우
            // .filter(m -> AnnotationUtils.findAnnotation(m, xunit.Annotation.Test.class) != null) // 스프링에서 사용, 애노테이션이 Test.class 인 경우 
            .forEach(m ->
                {
                    try {
                        add(testClass.getConstructor(String.class).newInstance(m.getName()));
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                }
            );
    }

    public void add(Test test) {
        tests.add(test);
    }

    public void run(TestResult result) {
        tests.forEach(t -> {
            t.run(result);
        });

    }
}

// TestCase만 사용하는 버전
// public class TestSuite {
//     List<TestCase> tests = new ArrayList<>();

//     public void add(TestCase test) {
//         tests.add(test);
//     }

//     public void run(TestResult result) {
//         tests.forEach(t -> {
//             t.run(result);
//         });

//     }
// }
