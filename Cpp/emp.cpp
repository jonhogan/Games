#include <iostream>
#include <string>
using namespace std;

class employee
{ 
    int age;
    int emp_id;
    string name;
    double salary;
    string city;
    string state;
    string street_address;
    string zip_code;
    public:
    void set_age(int a)
    {
        age = a;
    }
    void set_emp_id(int id)
    {
        emp_id = id;
    }
    void set_name(string n)
    {
        name = n;
    }
    void set_salary(double s)
    {
        salary = s;
    }
    void set_city(string c)
    {
        city = c;
    }
    void set_state(string s)
    {
        state = s;
    }
    void set_street_address(string s)
    {
        street_address = s;
    }
    void set_zip_code(string z)
    {
        zip_code = z;
    }
    int get_age()
    {
        return age;
    }
    int get_emp_id()
    {
        return emp_id;
    }
    string get_name()
    {
        return name;
    }
    double get_salary()
    {
        return salary;
    }
    string get_city()
    {
        return city;
    }
    string get_state()
    {
        return state;
    }
    string get_street_address()
    {
        return street_address;
    }
    string get_zip_code()
    {
        return zip_code;
    }

};

int main()
{
    employee emp[5];
    int i;
    for(i=0;i<5;i++)
    {
        int age;
        int emp_id;
        string name;
        double salary;
        string city;
        string state;
        string street_address;
        string zip_code;
        cout<<"Enter the details of employee "<<i+1<<endl;
        cout<<"Enter the age of employee "<<i+1<<endl;
        cin>>age;
        emp[i].set_age(age);
        cout<<"Enter the employee id of employee "<<i+1<<endl;
        cin>>emp_id;
        emp[i].set_emp_id(emp_id);
        cout<<"Enter the name of employee "<<i+1<<endl;
        cin>>name;
        emp[i].set_name(name);
        cout<<"Enter the salary of employee "<<i+1<<endl;
        cin>>salary;
        emp[i].set_salary(salary);
        cout<<"Enter the city of employee "<<i+1<<endl;
        cin>>city;
        emp[i].set_city(city);
        cout<<"Enter the state of employee "<<i+1<<endl;
        cin>>state;
        emp[i].set_state(state);
        cout<<"Enter the street address of employee "<<i+1<<endl;
        cin>>street_address;
        emp[i].set_street_address(street_address);
        cout<<"Enter the zip code of employee "<<i+1<<endl;
        cin>>zip_code;
        emp[i].set_zip_code(zip_code);
    }   
    for(i=0;i<5;i++)
    {
        cout<<"The details of employee "<<i+1<<" are as follows"<<endl;
        cout<<"Age: "<<emp[i].get_age()<<endl;
        cout<<"Employee id: "<<emp[i].get_emp_id()<<endl;
        cout<<"Name: "<<emp[i].get_name()<<endl;
        cout<<"Salary: "<<emp[i].get_salary()<<endl;
        cout<<"City: "<<emp[i].get_city()<<endl;
        cout<<"State: "<<emp[i].get_state()<<endl;
        cout<<"Street address: "<<emp[i].get_street_address()<<endl;
        cout<<"Zip code: "<<emp[i].get_zip_code()<<endl;
    }
    return 0;
}