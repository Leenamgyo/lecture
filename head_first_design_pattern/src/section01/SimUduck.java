package section01;

public class SimUduck {
    public static void main(String[] args) {
        
    }
}



abstract class Duck {
    public void quack() {
        System.out.println("quack");
    }

    public void swim() {
        System.out.println("swim");
    }

    public void fly() {
        System.out.println("fly");
    }

    abstract public void display();
}

class MallardDuck extends Duck {
    public void display() {
        System.out.println("MallardDuck");
    }
}


class RedheadDuck extends Duck {
    public void display() {
        System.out.println("MallardDuck");
    }
}