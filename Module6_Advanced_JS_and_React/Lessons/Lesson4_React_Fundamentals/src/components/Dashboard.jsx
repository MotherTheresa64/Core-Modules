import Profile from './Profile';

function Dashboard() {
  return (
    <div>
      <Profile />
      <p>I’m currently learning the fundamentals of React through Coding Temple.</p>
      <button onClick={() => alert("Thanks for clicking!")}>Click Me</button>
    </div>
  );
}

export default Dashboard;
