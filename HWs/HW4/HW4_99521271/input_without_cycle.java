// Class representing a University that is coupled with the City class
class University {
    private String ID;
    private String name;
    private City city;

    public University(String ID, String name, City city) {
        this.ID = ID;
        this.name = name;
        this.city = city;
    }

}

// Class representing a Student that is coupled with the University class
class Student {
    private String FirstName;
    private String LastName;
    private University uni;

    public Student(String FirstName, String LastName, University uni) {
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.uni = uni;
    }
}

// Class representing a City
class City {
    private String name;

    public City(String name) {
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) {
        City city = new City("tehran");

        // Creating an instance of the University class
        University uni = new University("12345678", "IUST", city);

        // Creating an instance of the Student class and associating it with the
        // University
        Student student = new Student("Farzan", "Rahmani", uni);
    }
}
