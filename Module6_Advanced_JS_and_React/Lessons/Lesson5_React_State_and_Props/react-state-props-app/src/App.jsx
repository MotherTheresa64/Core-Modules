import Counter from './components/Counter';
import MessageDisplay from './components/MessageDisplay';
import MessageList from './components/MessageList';

function App() {
  const message = "React makes building UI fun!";
  const users = ["Alice", "Bob", "Charlie"];

  return (
    <div className="app">
      <h1>Lesson 5: State & Props</h1>
      <Counter />
      <MessageDisplay message={message} />
      <MessageList users={users} />
    </div>
  );
}

export default App;
