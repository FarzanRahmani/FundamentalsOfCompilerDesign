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

    public Student(String FirstName, String LastName) {
        this.FirstName = FirstName;
        this.LastName = LastName;
    }

    public void AddUniversity(University uni) {
        this.uni = uni;
    }
}

// Class representing a City that is coupled with the Student class
class City {
    private String name;
    private Student student;

    public City(String name, Student student) {
        this.name = name;
        this.student = student;
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an instance of the Student class
        Student student = new Student("Farzan", "Rahmani");

        City city = new City("tehran", student);

        // Creating an instance of the University class
        University uni = new University("12345678", "IUST", city);

        // and associating Student with the University
        student.AddUniversity(uni);
    }
}
