package section01;

public class SimUduck2 {
    public static void main(String[] args) {
        
    }
}



abstract class Duck {
    // public void quack() {
    //     System.out.println("quack");
    // }

    public void swim() {
        System.out.println("swim");
    }

    // public void fly() {
    //     System.out.println("fly");
    // }

    abstract public void display();
}

interface FlyBehavior {
    public void fly();
}

interface QuackBehavior {
    public void quack();
}

class FlyWithWings implements FlyBehavior{
    @Override
    public void fly() {
        System.out.println("flyWithWings");
    }
}

class FlyNoWay implements FlyBehavior{
    @Override
    public void fly() {
        System.out.println("FlyNoWay");
    }
}

class Quack implements QuackBehavior {
    @Override
    public void quack() {
        System.out.println("꽥꽥");
    }
}

class MuteQuack implements QuackBehavior {
    @Override
    public void quack() {
        System.out.println("XX");
    }
}


class Squeak implements QuackBehavior {
    @Override
    public void quack() {
        System.out.println("삑삑");
    }
}

class MallardDuck extends Duck implements Flyable, Quackable {
    public void display() {
        System.out.println("MallardDuck");
    }
    @Override
    public void fly() {
        System.out.println("fly");
    }

    @Override
    public void quack() {
        System.out.println("quack");
    }
}
class RedheadDuck extends Duck implements Flyable, Quackable {
    public void display() {
        System.out.println("MallardDuck");
    }
    @Override
    public void fly() {
        System.out.println("fly");
    }

    @Override
    public void quack() {
        System.out.println("quack");
    }
}
class RubberDuck extends Duck implements Quackable {
    public void display() {
        System.out.println("RubberDuck");
    }

    @Override
    public void quack() {
        System.out.println("quack");
    }
}
class DecoyDuck extends Duck {
    public void display() {
        System.out.println("DecoyDuck");
    }
}