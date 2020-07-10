
class Employee:
    def __init__(self, eid, ename, erole, esalary):
        self.emp_id=eid
        self.emp_name=ename
        self.emp_role=erole
        self.emp_salary=esalary
    
    def increament_salary(self, percent):
        return self.emp_salary*percent*0.01
class Oraganization:
    def __init__(self,oname, elist):
        self.org_name=oname
        self.emp_list=elist
    def calculate_increament(self, role, percent):
        emp_res=[]
        for emp in self.emp_list:
            if emp.emp_role == role:
                emp.increament_salary(percent)
                emp_res.append(emp)
        return emp_res

if __name__ == '__main__':
    count=int(input())
    elist=[]
    for i in range(count):
        eid=int(input())
        ename=input()
        erole=input()
        esalary=int(input())
        elist.append(Employee(eid,ename,erole,esalary))
    org=Oraganization("XYZ Corp", elist)
    role=input()
    salary=int(input())
    e_res=org.calculate_increament(role, salary)
    if len(e_res) != 0:
        for emp in e_res:
            print(emp.emp_name,'\t',emp.emp_salary)
    else:
        print("No Employee Found With Given Role")
    
