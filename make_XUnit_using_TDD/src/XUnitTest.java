public class XUnitTest {
    public static void main(String[] args) {
        // new TestCaseTest("testTemplateMethod").run();
        // new TestCaseTest("testResult").run();
        // new TestCaseTest("testFailedResultFormatting").run();
        // new TestCaseTest("testFailedResult").run();

        // Summary를 가져오려면? 그러나 가독성도 안좋고 일일히 모든 구문마다 sysout을 호출하는 것은 너무 불편하다.
        // System.out.println(new TestCaseTest("testFailedResult").run().getSummary());
        // testSuite를 만들어보자 

        // TestResult result = new TestResult();
        // new TestCaseTest("testTemplateMethod").run(result);
        // new TestCaseTest("testResult").run(result);
        // new TestCaseTest("testFailedResultFormatting").run(result);
        // new TestCaseTest("testFailedResult").run(result);
        // new TestCaseTest("testSuite").run(result);
        // System.out.println(result.getSummary());

        //만든 testSuite으로 run메소드를 다 없애보자  
        // TestSuite suite = new TestSuite();
        // suite.add(new TestCaseTest("testTemplateMethod"));
        // suite.add(new TestCaseTest("testResult"));
        // suite.add(new TestCaseTest("testFailedResultFormatting"));
        // suite.add(new TestCaseTest("testFailedResult"));
        // suite.add(new TestCaseTest("testSuite"));
        // TestResult result = new TestResult();
        // suite.run(result);
        // System.out.println(result.getSummary());

        // suite.add를 캡슐화 해보자 
        TestSuite suite = TestCaseTest.suite();
        TestResult result = new TestResult();
        suite.run(result);
        System.out.println(result.getSummary());

        
        // suite 안에 suite을 넣는 것 
        // TestCase, TestSuite 모두 Test라는 것으로 퉁친다.
        // 즉, Test라는 인터페이스를 만들어 이 인터페이스를 구성하는 것을 모두 실행시킬 수 있는 모듈로 변경한다.
        // TestSuite suite2 = new TestSuite();
        // suite2.add(new TestCaseTest("testTemplateMethod"));
        // suite2.add(suite);
        
        // TestResult result2 = new TestResult();
        // suite2.run(result2);
        // System.out.println(result2.getSummary());
    }
}