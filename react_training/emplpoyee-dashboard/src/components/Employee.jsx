function Employee(props) {
  return (
    <>
      <h2>Employee Details</h2>
      <p>Name : {props.employeeName}</p>
      <p>Department : {props.department}</p>
      <p>Salary : ₹{props.salary}</p>
      <p>Permanent : {props.isPermanent ? "Yes" : " No"}</p>
    </>
  );
}

export default Employee;
